#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import velchange as v
from roboclaw import *
import math
import time

status = 0;

class Statics:
	status = int(0)
	old_X_Pos = float(0)
	old_Y_Pos = float(0)
	oldAnglePos = float(0)

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    defendGoal(data.data)
    rushBall(data.data)

def defendGoal(data):
	#break off the information
	myList = data.split("\n")
	robotInfo = myList[0].split(",")
	ballInfo = myList[1].split(",")
	
	#break off to variables
	robotX = float(robotInfo[0]);
	robotY = float(robotInfo[1]);
	theta = float(robotInfo[2]);
	ballX = float(ballInfo[0])
	ballY = float(ballInfo[1])

	commanded_X_pos = 1.66
	if (ballY > .25):
		commanded_Y_pos = .25
	elif (ballY < -.25):
		commanded_Y_pos = -.25
	else:
		commanded_Y_pos = ballY

	current_X_pos = float(robotX)
	current_Y_pos = float(robotY)
	current_Ang_pos = float(theta)

	XErr = commanded_X_pos - current_X_pos
	YChange = current_Y_pos - Statics.old_Y_Pos
	YErr = commanded_Y_pos - current_Y_pos

	flag = False;
 
	#and (current_Y_pos > -.25 and current_Y_pos < .25)

	if (abs(YErr) > 0.05 ):
		flag = True;
	
	if (flag):

		error_Max_X = .5
		vel_Max_X = 1
		error_X = XErr
		kp_X = float(vel_Max_X)/float(error_Max_X) # units don't match, but that's okay
		vel_X = kp_X*error_X

		error_Max_Y = .5
		vel_Max_Y = 1
		error_Y = YErr
		kp_Y = float(vel_Max_Y)/float(error_Max_Y) # units don't match, but that's okay
		vel_Y = kp_Y*error_Y

		vel_X_Body_Frame = math.cos(theta)*vel_X + math.sin(theta)*vel_Y 
		vel_Y_Body_Frame = -1*(math.cos(theta)*vel_Y - math.sin(theta)*vel_X)

		print data
		print "error in X %f"%error_X
		print "current_X_pos %f"%current_X_pos
		print "vel X %f"%vel_X
		print
		print "current_Y_pos %f"%current_Y_pos
		print "error in Y %f"%error_Y
		print "vel Y %f"%vel_Y



		print "vel x body frame %f"%vel_X_Body_Frame
		print "vel y body frame %f"%vel_Y_Body_Frame

		

		v.goVel(vel_X_Body_Frame, vel_Y_Body_Frame, 0)
	else:
		v.goVel(0,0,0)

	# if (ballY > robotY):
	# 	goRight()
	# else
	# 	goLeft()

def rushBall(data):
	#break off the information
	myList = data.split("\n")
	robotInfo = myList[0].split(",")
	ballInfo = myList[1].split(",")
	
	#break off to variables
	robotX = robotInfo[0];
	robotY = robotInfo[1];
	theta = float(robotInfo[2]);
	ballX = float(ballInfo[0])
	ballY = float(ballInfo[1])
	# print robotX
	# print robotY
	# print theta
	# convert to floats
	commanded_X_pos = float(ballX)
	commanded_Y_pos = float(ballY)
	commanded_Ang_pos = float(0)
	current_X_pos = float(robotX)
	current_Y_pos = float(robotY)
	current_Ang_pos = float(theta)

	XChange = current_X_pos - Statics.old_X_Pos
	YChange = current_Y_pos - Statics.old_Y_Pos
	AngleChange = current_Ang_pos - Statics.oldAnglePos
	XErr = commanded_X_pos - current_X_pos
	YErr = commanded_Y_pos - current_Y_pos
	AngleErr = commanded_Ang_pos - current_Ang_pos

	flag = False;

	if (abs(XErr) > 0.1 or abs(YErr) > 0.1 or abs(AngleErr) > 0.2):
		flag = True;
	
	if (flag):
		error_Max_X = 2
		vel_Max_X = 1
		error_X = XErr
		kp_X = float(vel_Max_X)/float(error_Max_X) # units don't match, but that's okay
		vel_X = kp_X*error_X

		error_Max_Y = 2
		vel_Max_Y = 1
		error_Y = YErr
		kp_Y = float(vel_Max_Y)/float(error_Max_Y) # units don't match, but that's okay
		vel_Y = kp_Y*error_Y

		vel_Ang = 0
		error_Ang = 0
		if (abs(AngleErr) > 0.2):
			error_Max_Ang = 3.14 #in radians
			vel_Max_Ang = 1
			error_Ang = AngleErr
			kp_Ang = float(vel_Max_Ang)/float(error_Max_Ang) # units don't match, but that's okay
			vel_Ang = kp_Ang*error_Ang

		theta_Damped = theta - vel_Ang/4
		vel_X_Body_Frame = math.cos(theta)*vel_X + math.sin(theta)*vel_Y 
		vel_Y_Body_Frame = -1*(math.cos(theta)*float(vel_Y) - math.sin(theta)*float(vel_X))


		print data
		print "error in X %f"%error_X
		print "current_X_pos %f"%current_X_pos
		print "vel X %f"%vel_X
		print
		print "error in Y %f"%error_Y
		print "current_Y_pos %f"%current_Y_pos
		print "vel Y %f"%vel_Y
		print
		print "error in angle %f"%error_Ang
		print "current Angle %f"%current_Ang_pos
		print "angle vel %f"%vel_Ang

		print "damped angle %f"%theta_Damped


		print "vel x body frame %f"%vel_X_Body_Frame
		print "vel y body frame %f"%vel_Y_Body_Frame

		

		v.goVel(vel_X_Body_Frame, vel_Y_Body_Frame, 0)
	else:
		v.goVel(0,0,0)
	

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('vision', String, callback)
    if (status == 1):
    	return
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
	SetM2pidq(128,65536,32768,16384,243759)
	SetM2pidq(129,65536,32768,16384,264568)
	SetM1pidq(129,65536,32768,16384,256704)
	#v.myCircle()
	#v.mySquare()
	listener()
