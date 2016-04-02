#!/usr/bin/env python
import argparse

import rospy
from std_msgs.msg import Float64MultiArray
import velchange as v
from roboclaw import *
import math
import time
import sys

class stopper:
	def __init__(self):
		self.args = None
		self.robotX = None
		self.robotY = None
		self.theta = None
		self.sideOfField = None
		self.state = None

		self.parse_arguments()

	def parse_arguments(self):
		parser = argparse.ArgumentParser(prog='Stopper', description='a program that resets the robot to start and stops it', add_help=True)
		parser.add_argument('-s', '--side', type=str, action='store', help='Specify the side of field that you are playing',default="Away")

		args = parser.parse_args()
		self.sideOfField = args.side
		self.state = "goBackToBeginning"

	def callback(self, data):
		# Print information received from vision
		#rospy.loginfo(rospy.get_caller_id() + 'I heard %f, %f, %f, %f, %f', data.data[0], data.data[1], data.data[2], data.data[3], data.data[4])

		# Grab variables from vision
		self.robotX = float(data.data[0])
		self.robotY = float(data.data[1])
		self.theta = float(data.data[2])

		# Call the state machine to decide what to do based on data
		self.stateMachine()

	def stateMachine(self):
		if (self.state == "goBackToBeginning"):
			self.goBackToBeginning()
		else:
			self.correctAngle()

	def correctAngle(self):
		# Define where the enemy goal lies
		if (self.sideOfField == "Away"):
			enemyGoalCenterX = 1.4
		else:
			enemyGoalCenterX = -1.29
		enemyGoalCenterY = 0
		deltaX = enemyGoalCenterX - self.robotX
		deltaY = enemyGoalCenterY - self.robotY
		commanded_Ang_pos = float(math.atan2(deltaY, deltaX))
		if (commanded_Ang_pos < 0):
			commanded_Ang_pos += (math.pi*2)
		
		# Calculate the Error in the angle position from the desired
		AngleErr = commanded_Ang_pos - self.theta

		#check for smallest angle to commanded ang
		if (AngleErr > math.pi):
			AngleErr = AngleErr - math.pi*2
		elif (AngleErr < -math.pi):
			AngleErr = AngleErr + math.pi*2

		# Code for Proportional Controller for Angle
		error_Max_Ang = 3.14 #in radians
		vel_Max_Ang = 2.9;
		error_Ang = AngleErr
		kp_Ang = float(vel_Max_Ang)/float(error_Max_Ang) # units don't match, but that's okay
		vel_Ang = kp_Ang*error_Ang

		# Send commands to the wheels
		v.goVel(0.0, 0.0, vel_Ang)

		# If Error is small, then the robot is facing the goal, so transition to attack
		if (abs(AngleErr) <= 0.25):
			v.goVel(0.0,0.0,0.0)
		return

	def goBackToBeginning(self):
		if (self.sideOfField == "Away"):
			commandedX = -0.535
		else:
			commandedX = 0.535
		commandedY = 0.0
		XErr = commandedX - self.robotX
		YErr = commandedY - self.robotY

		# Code for Proportional Controller for X
		error_Max_X = 2.0
		vel_Max_X = 1.45
		error_X = XErr
		kp_X = float(vel_Max_X)/float(error_Max_X) # units don't match, but that's okay
		vel_X = kp_X*error_X

		# Code for Proportional Controller for Y
		error_Max_Y = 2.0
		vel_Max_Y = 1.45
		error_Y = YErr
		kp_Y = float(vel_Max_Y)/float(error_Max_Y) # units don't match, but that's okay
		vel_Y = kp_Y*error_Y

		# Account for the angle of the robot
		vel_X_Body_Frame = math.cos(self.theta)*vel_X + math.sin(self.theta)*vel_Y 
		vel_Y_Body_Frame = -1.0*(math.cos(self.theta)*float(vel_Y) - math.sin(self.theta)*float(vel_X))
		
		# Send commands to the wheels
		v.goVel(vel_X_Body_Frame, vel_Y_Body_Frame, 0.0)

		# If Error is small, then we are at the start, so stop robot
		if (abs(XErr) <= 0.1 and abs(YErr) <= 0.1):
			v.goVel(0.0,0.0,0.0)
			self.state = "correctAngle"
		return


	def listener(self):

		rospy.init_node('reset', anonymous=True)

		rospy.Subscriber('Vision', Float64MultiArray, self.callback)
		rospy.spin()


if __name__ == '__main__':
	# Calibrate wheels
	p = int(65536 * 4) #262144
	i = int(65536 * 2) #131072
	d = int(65536 * 6)  #65536
	SetM1pidq(129,p,i,d,158372)
	SetM2pidq(128,p,i,d,164501)
	SetM2pidq(129,p,i,d,141356)
	# SetM2pidq(128,65536,32768,16384,243759)
	# SetM2pidq(129,65536,32768,16384,264568)
	# SetM1pidq(129,65536,32768,16384,256704)
	# Setup some variables
	s = stopper()
	s.listener()