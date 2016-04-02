#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64MultiArray
import velchange as v
from roboclaw import *
import math
import time
import sys

######################################################################################################################################
##################################################### Static Variables ###############################################################
######################################################################################################################################

class Statics:
	# Varibles to setup up robot's initial state
	state = "rushBall"
	sideOfField = "Away"
	samples = 0;
	debug = 0;
	angleSamples = 0;
	xSamples = 0;
	ySamples = 0;
	suspendDefense = 0;
	showTransitions = 1;
	showDataReceived = 0;
	maxSamples = 10
	oldAngle = 0;
	oldX = 0;
	oldY = 0;

	# Data Received From Vision
	robotX = float(0)
	robotY = float(0)
	theta = float(0)
	ballX = float(0)
	ballY = float(0)

	# Helpful Variables
	enemyGoalCenterX = 0
	enemyGoalCenterY = 0
	XErr = 0
	YErr = 0
	AngleErr = 0
	commanded_Ang_pos = 0
	vel_X_Body_Frame = 0
	vel_Y_Body_Frame = 0

######################################################################################################################################
#################################################### ROS Call Back Function ##########################################################
######################################################################################################################################

def callback(data):
	# Print information received from vision
	if (Statics.showDataReceived):
		rospy.loginfo(rospy.get_caller_id() + 'I heard %f, %f, %f, %f, %f', data.data[0], data.data[1], data.data[2], data.data[3], data.data[4])

	# Parse the information received from vision
	parseData(data.data)

	# Call the state machine to decide what to do based on data
	stateMachine()

	# increment count of samples
	Statics.samples = Statics.samples + 1

######################################################################################################################################
######################################################### Data Parser ################################################################
######################################################################################################################################
def parseData(data):

	#break off to variables
	Statics.robotX = (data[0]);
	Statics.robotY = (data[1]);
	Statics.theta = (data[2]);
	Statics.ballX = (data[3])
	Statics.ballY = (data[4])

######################################################################################################################################
######################################################## State Machine ###############################################################
######################################################################################################################################
def selectState():	
	#######################################
	""" Case 1: we are in Go To Goal """
	#######################################
	if (Statics.state == "goToGoal"):
		# If the ball is far enough from our goal then we can stop defending and get back to rushing the ball
		if ((Statics.sideOfField == "Away" and Statics.ballX > -0.70) or (Statics.sideOfField == "Home" and Statics.ballX < 0.70)):
			Statics.state = "rushBall"
			if (Statics.showTransitions):
				print "Entering rush ball"

		commanded_Y_pos = 0.0
		if (Statics.sideOfField == "Away"):
			commanded_X_pos = float(-1.25)
		else:
			commanded_X_pos = float(1.35)

		# Calculate Error from desired positions
		Statics.XErr = commanded_X_pos - Statics.robotX
		Statics.YErr = commanded_Y_pos - Statics.robotY

		# If Error is small, then we are at the goal, transition to defend
		if (abs(Statics.XErr) <= 0.2 and abs(Statics.YErr) <= 0.2):
			v.goVel(0.0,0.0,0.0)
			Statics.state = "defendGoal"
			if (Statics.showTransitions):
				print "Entering Defend Goal"
		return
	
	#######################################
	""" Case 2: we are in Defend Goal """
	#######################################
	if (Statics.state == "defendGoal"):
		# Analyze current Status of the robot
		if (Statics.sideOfField == "Away"):
			commanded_X_pos = -1.25
		else:
			commanded_X_pos = 1.36

		if (Statics.ballY > .25):
			commanded_Y_pos = .25
		elif (Statics.ballY < -.25):
			commanded_Y_pos = -.25
		else:
			commanded_Y_pos = Statics.ballY

		# Calculate the Error from Desired Position
		Statics.XErr = commanded_X_pos - Statics.robotX
		Statics.YErr = commanded_Y_pos - Statics.robotY

		# If the ball is far from the goal, rush it
		if ((Statics.sideOfField == "Away" and Statics.ballX > -0.60) or (Statics.sideOfField == "Home" and Statics.ballX < 0.60)):
			Statics.state = "rushBall"
			if (Statics.showTransitions):
				print "Entering rush ball"
		
		# If the ball is really close to the robot, also rush it
		if (abs(Statics.ballX - Statics.robotX) < 0.2):
			Statics.state = "rushBall"	
			Statics.suspendDefense = 1
			if (Statics.showTransitions):
				print "Entering rush ball"
		# If the robot has reached where it is supposed to, stop it temporarily in that position
		if (abs(Statics.XErr) < 0.2):
			v.goVel(0.0, 0.0, 0.0);
		return

	#######################################
	""" Case 3: we are in attack Enemy """
	#######################################
	if (Statics.state == "attackEnemy"):
		# Analyze current status of robot
		if (Statics.sideOfField == "Away"):
			commanded_X_pos = 1.6
		else:
			commanded_X_pos = -1.49
		commanded_Y_pos = float(0)

		# If the ball is far from the robot, go back to rushing it
		BotBallDisX = abs(Statics.robotX - Statics.ballX)
		BotBallDisY = abs(Statics.robotY - Statics.ballY)
		if (Statics.debug):
			print "BotBallDist X is %f"%BotBallDisX
			print "BotBallDist Y is %f"%BotBallDisY

		if (BotBallDisX > 0.4 or BotBallDisY > 0.4):
			Statics.state = "rushBall"
			if (Statics.showTransitions):
				print "Entering rush ball"

		# Calculate the Error from the desired position
		Statics.XErr = commanded_X_pos - Statics.robotX
		Statics.YErr = commanded_Y_pos - Statics.robotY

		Statics.xSamples = Statics.xSamples+1;
		if (Statics.xSamples == 5):
			Statics.xSamples = 0;
			Statics.oldX = Statics.robotX;

		Statics.ySamples = Statics.ySamples+1;
		if (Statics.ySamples == 5):
			Statics.ySamples = 0;
			Statics.oldY = Statics.robotY;

		# If Error is small, then that means we scored a goal, transition back to rush ball
		if (abs(Statics.XErr) <= 0.15 and abs(Statics.YErr) <= 0.1):
			v.goVel(0.0,0.0,0.0)
			Statics.state = "rushBall"
			if (Statics.showTransitions):
				print "Entering rushball"
		return

	#######################################
	""" Case 4: we are in rush ball """
	#######################################
	if (Statics.state == "rushBall"):
		# If the ball is close to our goal, go back to defend it quickly
		if (not Statics.suspendDefense and (Statics.sideOfField == "Away" and Statics.ballX < -0.8) or (Statics.sideOfField == "Home" and Statics.ballX > 0.8)):
			Statics.state = "goToGoal"
			if (Statics.showTransitions):
				print "Entering Go To GOAL"

		# If the robot surpasses the defense threshold, unsuspend the defense
		if ((Statics.sideOfField == "Away" and Statics.robotX > -0.6) or (Statics.sideOfField == "Home" and Statics.robotX < 0.6)):
			Statics.suspendDefense = 0

		# Calculate a position that is about 0.2m behind the ball and go there
		deltaX = Statics.enemyGoalCenterX - Statics.ballX
		deltaY = Statics.enemyGoalCenterY - Statics.ballY
		commanded_X_pos = Statics.ballX + ((-0.2)*deltaX/math.sqrt(deltaX*deltaX + deltaY*deltaY)) 
		commanded_Y_pos = Statics.ballY + ((-0.2)*deltaY/math.sqrt(deltaX*deltaX + deltaY*deltaY)) 

		# Check if the robot is currently behind the ball
		if (Statics.sideOfField == "Home" and (Statics.ballX - Statics.robotX) < 0.0):
			robotBehindBall = 1
		elif (Statics.sideOfField == "Away" and (Statics.ballX - Statics.robotX) > 0.0):
			robotBehindBall = 1
		else:

			robotBehindBall = 0

		if (Statics.debug):
			print "ballX is %f and robot X is %f"%(Statics.ballX, Statics.robotX)

		# Calculate Error from desired
		Statics.XErr = commanded_X_pos - Statics.robotX
		Statics.YErr = commanded_Y_pos - Statics.robotY
		if (Statics.debug):
			print "error X is %f"%Statics.XErr
			print "error Y is %f"%Statics.YErr

		Statics.xSamples = Statics.xSamples+1;
		if (Statics.xSamples == 5):
			Statics.xSamples = 0;
			Statics.oldX = Statics.robotX;

		Statics.ySamples = Statics.ySamples+1;
		if (Statics.ySamples == 5):
			Statics.ySamples = 0;
			Statics.oldY = Statics.robotY;

		# If Error is small, then the robot is right behind the ball, so now correct angle
		if (abs(Statics.XErr) <= 0.1 and abs(Statics.YErr) <= 0.1 and robotBehindBall):# and abs(Statics.AngleErr) <= 0.5):
			v.goVel(0.0,0.0,0.0)
			Statics.state = "correctAngle"
			if (Statics.showTransitions):
				print "Entering correct Angle"
		return

	#######################################
	""" Case 5: we are in Correct Angle """
	#######################################
	if (Statics.state == "correctAngle"):
		calculateAngle()
		Statics.angleSamples = Statics.angleSamples+1;
		if (Statics.angleSamples == 5):
			Statics.angleSamples = 0;
			Statics.oldAngle = Statics.theta;

		# If Error is small, then the robot is facing the goal, so transition to attack
		if (abs(Statics.AngleErr) <= 0.25):
			v.goVel(0.0,0.0,0.0)
			# Kicker
			#kicker()
			Statics.state = "attackEnemy"
			if (Statics.showTransitions):
				print "Entering attack Enemy"
		return

def kicker():
	# Extend the kicker
	M1Forward(128, 127)
	time.sleep(0.1)
	# Retract the kicker
	M1Forward(128, 0)

def calculateAngle():
	# If we become away from the ball, then rush it to get back to a position close to it
	BotBallDisX = abs(Statics.robotX - Statics.ballX)
	BotBallDisY = abs(Statics.robotY - Statics.ballY)
	if (BotBallDisX > 0.5 or BotBallDisY > 0.5):
		Statics.state = "rushBall"
		if (Statics.showTransitions):
			print "Entering rush ball"

	# Analyze current status of robot
	deltaX = Statics.enemyGoalCenterX - Statics.ballX
	deltaY = Statics.enemyGoalCenterY - Statics.ballY
	Statics.commanded_Ang_pos = float(math.atan2(deltaY, deltaX))
	if (Statics.commanded_Ang_pos < 0):
		Statics.commanded_Ang_pos += (math.pi*2)
	
	# Calculate the Error in the angle position from the desired
	Statics.AngleErr = Statics.commanded_Ang_pos - Statics.theta

	#check for smallest angle to commanded ang
	if (Statics.AngleErr > math.pi):
		Statics.AngleErr = Statics.AngleErr - math.pi*2
	elif (Statics.AngleErr < -math.pi):
		Statics.AngleErr = Statics.AngleErr + math.pi*2

def stateMachine():
	selectState()
	if (Statics.state == "defendGoal"):
		defendGoal()
	elif (Statics.state == "rushBall"):
		rushBall()
	elif (Statics.state == "attackEnemy"):
		attackEnemy()
	elif (Statics.state == "correctAngle"):
		correctAngle()
	else:
		goToGoal()

######################################################################################################################################
########################################################### States ###################################################################
######################################################################################################################################		

def correctAngle():
	# Code for Proportional Controller for Angle
	error_Max_Ang = 3.14 #in radians
	if (abs(Statics.AngleErr) <= 0.5):
		vel_Max_Ang = 1.5;
	else:
		vel_Max_Ang = 3.14;
	if (abs(Statics.theta - Statics.oldAngle) < 0.1):
		vel_Max_Ang = 4.0
	error_Ang = Statics.AngleErr
	kp_Ang = float(vel_Max_Ang)/float(error_Max_Ang) # units don't match, but that's okay
	vel_Ang = kp_Ang*error_Ang

	# Send commands to the wheels
	v.goVel(0.0, 0.0, vel_Ang)

	# Print Data
	if (Statics.debug):
		print "commanded_Ang_pos is %f"%Statics.commanded_Ang_pos
		print "error in angle %f"%error_Ang
		print "current Angle %f"%Statics.theta
		print "angle vel %f"%vel_Ang


def goToGoal():
	# Code for Proportional Controller for X
	error_Max_X = 2.0
	vel_Max_X = 1.0
	error_X = Statics.XErr
	kp_X = float(vel_Max_X)/float(error_Max_X) # units don't match, but that's okay
	vel_X = kp_X*error_X

	# Code for Proportional Controller for Y
	error_Max_Y = 2.0
	vel_Max_Y = 1.0
	error_Y = Statics.YErr
	kp_Y = float(vel_Max_Y)/float(error_Max_Y) # units don't match, but that's okay
	vel_Y = kp_Y*error_Y

	# Account for the angle of the robot
	vel_X_Body_Frame = math.cos(Statics.theta)*vel_X + math.sin(Statics.theta)*vel_Y 
	vel_Y_Body_Frame = -1.0*(math.cos(Statics.theta)*float(vel_Y) - math.sin(Statics.theta)*float(vel_X))
	
	# Send commands to the wheels
	v.goVel(vel_X_Body_Frame, vel_Y_Body_Frame, 0.0)

	# Print Data
	if (Statics.debug and Statics.samples == Statics.maxSamples):
		Statics.samples = 0;
		print "error in X %f"%error_X
		print "current_X_pos %f"%Statics.robotX
		print "vel X %f"%vel_X
		print
		print "error in Y %f"%error_Y
		print "current_Y_pos %f"%Statics.robotY
		print "vel Y %f"%vel_Y
		print
		print "vel x body frame %f"%vel_X_Body_Frame
		print "vel y body frame %f"%vel_Y_Body_Frame


def defendGoal():
	# Code for Proportional Controller
	error_Max_X = .5
	vel_Max_X = 1.0
	error_X = Statics.XErr
	kp_X = float(vel_Max_X)/float(error_Max_X) # units don't match, but that's okay
	vel_X = kp_X*error_X

	# Code for Proportional Controller
	error_Max_Y = .5
	vel_Max_Y = 1.0
	error_Y = Statics.YErr
	kp_Y = float(vel_Max_Y)/float(error_Max_Y) # units don't match, but that's okay
	vel_Y = kp_Y*error_Y

	# Account for angle of the robot
	vel_X_Body_Frame = math.cos(Statics.theta)*vel_X + math.sin(Statics.theta)*vel_Y 
	vel_Y_Body_Frame = -1.0*(math.cos(Statics.theta)*vel_Y - math.sin(Statics.theta)*vel_X)

	# Send Commands to wheels
	v.goVel(vel_X_Body_Frame, vel_Y_Body_Frame, 0.0)

	# Print Data
	if (Statics.debug and Statics.samples == Statics.maxSamples):
		Statics.samples = 0;
		print "error in X %f"%error_X
		print "current_X_pos %f"%Statics.robotX
		print "vel X %f"%vel_X
		print
		print "current_Y_pos %f"%Statics.robotY
		print "error in Y %f"%error_Y
		print "vel Y %f"%vel_Y

		print "vel x body frame %f"%vel_X_Body_Frame
		print "vel y body frame %f"%vel_Y_Body_Frame


def attackEnemy():
	# Code for Proportional Controller
	if (abs(Statics.XErr) <= 0.5):
		error_Max_X = 1.6
		if (abs(Statics.robotX - Statics.oldX) < 0.5):
			error_Max_X = 1.3
	else:
		error_Max_X = 2.0
	vel_Max_X = 1.4
	error_X = Statics.XErr
	kp_X = float(vel_Max_X)/float(error_Max_X) # units don't match, but that's okay
	vel_X = kp_X*error_X

	# Code for Proportional Controller
	if (abs(Statics.YErr) <= 0.5):
		error_Max_Y = 1.6
		if (abs(Statics.robotY - Statics.oldY) < 0.5):
			error_Max_Y = 1.3
	else:
		error_Max_Y = 2.0
	vel_Max_Y = 1.4
	error_Y = Statics.YErr
	kp_Y = float(vel_Max_Y)/float(error_Max_Y) # units don't match, but that's okay
	vel_Y = kp_Y*error_Y

	# Account for angle of robot
	vel_X_Body_Frame = math.cos(Statics.theta)*vel_X + math.sin(Statics.theta)*vel_Y 
	vel_Y_Body_Frame = -1.0*(math.cos(Statics.theta)*float(vel_Y) - math.sin(Statics.theta)*float(vel_X))
	
	# Send Commands to Wheels
	v.goVel(vel_X_Body_Frame, vel_Y_Body_Frame, 0.0)

	# Print Data
	if (Statics.debug and Statics.samples == Statics.maxSamples):
		Statics.samples = 0
		print "error in X %f"%error_X
		print "current_X_pos %f"%Statics.robotX
		print "vel X %f"%vel_X
		print
		print "error in Y %f"%error_Y
		print "current_Y_pos %f"%Statics.robotY
		print "vel Y %f"%vel_Y

		print "vel x body frame %f"%vel_X_Body_Frame
		print "vel y body frame %f"%vel_Y_Body_Frame
		
def rushBall():
	# Code for Proportional Controller
	if (abs(Statics.XErr) <= 0.5):
		error_Max_X = 1.6
		if (abs(Statics.robotX - Statics.oldX) < 0.5):
			error_Max_X = 1.3
	else:
		error_Max_X = 2.0
	vel_Max_X = 1.4
	error_X = Statics.XErr
	kp_X = float(vel_Max_X)/float(error_Max_X) # units don't match, but that's okay
	vel_X = kp_X*error_X

	# Code for Proportional Controller
	if (abs(Statics.YErr) <= 0.5):
		error_Max_Y = 1.6
		if (abs(Statics.robotY - Statics.oldY) < 0.5):
			error_Max_Y = 1.3
	else:
		error_Max_Y = 2.0
	vel_Max_Y = 1.4
	error_Y = Statics.YErr
	kp_Y = float(vel_Max_Y)/float(error_Max_Y) # units don't match, but that's okay
	vel_Y = kp_Y*error_Y

	# Account for Angle
	Statics.vel_X_Body_Frame = math.cos(Statics.theta)*vel_X + math.sin(Statics.theta)*vel_Y 
	Statics.vel_Y_Body_Frame = -1*(math.cos(Statics.theta)*float(vel_Y) - math.sin(Statics.theta)*float(vel_X))

	#if we are close to ball and vel x and y are too small
	#Rerror = math.sqrt(error_X*error_X + error_Y*error_Y)
	# if(Rerror < .2):
	# 	radius_Error_Min = .2
	# 	Statics.vel_X_Body_Frame = kp_X * .2 * error_X/Rerror
	# 	Statics.vel_Y_Body_Frame = kp_Y * .2 * error_Y/Rerror

	# Send Commands to Wheels
	v.goVel(Statics.vel_X_Body_Frame, Statics.vel_Y_Body_Frame, 0.0)

	# Print Data
	if (Statics.debug):
		Statics.samples = 0
		print "error in X %f"%error_X
		print "current_X_pos %f"%Statics.robotX
		print "vel X %f"%vel_X
		print
		print "error in Y %f"%error_Y
		print "current_Y_pos %f"%Statics.robotY
		print "vel Y %f"%vel_Y
		print

		print "vel x body frame %f"%Statics.vel_X_Body_Frame
		print "vel y body frame %f"%Statics.vel_Y_Body_Frame

######################################################################################################################################
######################################################### Main Code ##################################################################
######################################################################################################################################
def setupField():
	# Define where the enemy goal lies
	if (Statics.sideOfField == "Away"):
		Statics.enemyGoalCenterX = 1.4
	else:
		Statics.enemyGoalCenterX = -1.29

def listener():

	rospy.init_node('listener', anonymous=True)

	rospy.Subscriber('Vision', Float64MultiArray, callback)
	rospy.spin()

if __name__ == '__main__':
	# Calibrate wheels
	p = int(65536 * 4) #262144
	i = int(65536 * 2) #131072
	d = int(65536 * 6)  #65536
	SetM1pidq(129,p,i,d,158372)
	SetM2pidq(128,p,i,d,164501)
	SetM2pidq(129,p,i,d,141356)

	# Setup some variables
	setupField()
	listener()
