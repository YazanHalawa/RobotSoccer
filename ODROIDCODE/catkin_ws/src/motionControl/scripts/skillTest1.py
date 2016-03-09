#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import velchange as v
from roboclaw import *
import math
import time

debug = 1
maxSamples = 10

class Statics:
	status = int(0)
	old_X_Pos = float(0)
	old_Y_Pos = float(0)
	oldAnglePos = float(0)
	state = "rushBall"
	sideOfField = "Away"
	samples = 0;

def callback(data):
	#if (debug == 1):
	#	rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
	if (Statics.state == "defendGoal"):
		defendGoal(data.data)
	elif (Statics.state == "rushBall"):
		rushBall(data.data)
	elif (Statics.state == "attackEnemy"):
		attackEnemy(data.data)
	else:
		goToGoal(data.data)
	Statics.samples = Statics.samples + 1
def goToGoal(data):


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



	if ((Statics.sideOfField == "Away" and ballX > -0.70) or (Statics.sideOfField == "Home" and ballX < 0.70)):
		print "Entering rush ball"
		Statics.state = "rushBall"

	if (Statics.sideOfField == "Away"):
		commanded_X_pos = float(-1.35)
	else:
		commanded_X_pos = float(1.35)

	# convert to floats
	commanded_Y_pos = float(0)
	commanded_Ang_pos = float(0)
	current_X_pos = float(robotX)
	current_Y_pos = float(robotY)
	current_Ang_pos = float(theta)

	XErr = commanded_X_pos - current_X_pos
	YErr = commanded_Y_pos - current_Y_pos
	AngleErr = commanded_Ang_pos - current_Ang_pos

	flag = False;

	if (abs(XErr) > 0.1 or abs(YErr) > 0.1):
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

		# vel_Ang = 0
		# error_Ang = 0
		# if (abs(AngleErr) > 0.2):
		# 	error_Max_Ang = 3.14 #in radians
		# 	vel_Max_Ang = 1
		# 	error_Ang = AngleErr
		# 	kp_Ang = float(vel_Max_Ang)/float(error_Max_Ang) # units don't match, but that's okay
		# 	vel_Ang = kp_Ang*error_Ang
		#theta_Damped = theta - vel_Ang/4

		vel_X_Body_Frame = math.cos(theta)*vel_X + math.sin(theta)*vel_Y 
		vel_Y_Body_Frame = -1*(math.cos(theta)*float(vel_Y) - math.sin(theta)*float(vel_X))


		if (debug == 1 and Statics.samples == maxSamples):
			Statics.samples = 0;
			print data
			print "error in X %f"%error_X
			print "current_X_pos %f"%current_X_pos
			print "vel X %f"%vel_X
			print
			print "error in Y %f"%error_Y
			print "current_Y_pos %f"%current_Y_pos
			print "vel Y %f"%vel_Y
			print
			# print "error in angle %f"%(error_Ang*float(180)/float(math.pi))
			# print "current Angle %f"%(current_Ang_pos*float(180)/float(math.pi))
			# print "angle vel %f"%vel_Ang

			#print "damped angle %f"%theta_Damped


			print "vel x body frame %f"%vel_X_Body_Frame
			print "vel y body frame %f"%vel_Y_Body_Frame

		

		v.goVel(vel_X_Body_Frame, vel_Y_Body_Frame, 0)
	else:
		v.goVel(0,0,0)
		print "Entering Defend Goal"
		Statics.state = "defendGoal"


def defendGoal(data):

	#break off the information
	myList = data.split("\n")
	robotInfo = myList[0].split(",")
	ballInfo = myList[1].split(",")

	#break off to variables
	robotX = float(robotInfo[0])
	robotY = float(robotInfo[1])
	theta = float(robotInfo[2])
	ballX = float(ballInfo[0])
	ballY = float(ballInfo[1])

	if (Statics.sideOfField == "Away"):
		commanded_X_pos = -1.35
	else:
		commanded_X_pos = 1.35

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
	YErr = commanded_Y_pos - current_Y_pos

	flag = False;
 
	#and (current_Y_pos > -.25 and current_Y_pos < .25)

	if (abs(XErr) > 0.1 or abs(YErr) > 0.05 ):
		flag = True;
	
	if (abs(ballX - robotX) < 0.2):
		print "Entering Rush Ball"
		Statics.state = "rushBall"

	if (flag):

		error_Max_X = 2#.5
		vel_Max_X = 1
		error_X = XErr
		kp_X = float(vel_Max_X)/float(error_Max_X) # units don't match, but that's okay
		vel_X = kp_X*error_X

		error_Max_Y = 2#.5
		vel_Max_Y = 1
		error_Y = YErr
		kp_Y = float(vel_Max_Y)/float(error_Max_Y) # units don't match, but that's okay
		vel_Y = kp_Y*error_Y

		vel_X_Body_Frame = math.cos(theta)*vel_X + math.sin(theta)*vel_Y 
		vel_Y_Body_Frame = -1*(math.cos(theta)*vel_Y - math.sin(theta)*vel_X)

		if (debug == 1 and Statics.samples == maxSamples):
			Statics.samples = 0;
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

def attackEnemy(data):

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


	commanded_X_pos = 0
	if (Statics.sideOfField == "Away"):
		commanded_X_pos = 1.6
	else:
		commanded_X_pos = -1.6

	# convert to floats
	commanded_Y_pos = float(0)
	current_X_pos = float(robotX)
	current_Y_pos = float(robotY)
	current_Ang_pos = float(theta)

	XErr = commanded_X_pos - current_X_pos
	YErr = commanded_Y_pos - current_Y_pos

	flag = False;

	if (abs(XErr) > 0.1 or abs(YErr) > 0.1):
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

		# vel_Ang = 0
		# error_Ang = 0
		# if (abs(AngleErr) > 0.2):
		# 	error_Max_Ang = 3.14 #in radians
		# 	vel_Max_Ang = 1
		# 	error_Ang = AngleErr
		# 	kp_Ang = float(vel_Max_Ang)/float(error_Max_Ang) # units don't match, but that's okay
		# 	vel_Ang = kp_Ang*error_Ang

		# theta_Damped = theta - vel_Ang/4
		vel_X_Body_Frame = math.cos(theta)*vel_X + math.sin(theta)*vel_Y 
		vel_Y_Body_Frame = -1*(math.cos(theta)*float(vel_Y) - math.sin(theta)*float(vel_X))


		if (debug == 1 and Statics.samples == maxSamples):
			Statics.samples = 0
			print data
			print "error in X %f"%error_X
			print "current_X_pos %f"%current_X_pos
			print "vel X %f"%vel_X
			print
			print "error in Y %f"%error_Y
			print "current_Y_pos %f"%current_Y_pos
			print "vel Y %f"%vel_Y
			# print
			# print "error in angle %f"%(error_Ang*float(180)/float(math.pi))
			# print "current Angle %f"%(current_Ang_pos*float(180)/float(math.pi))
			# print "angle vel %f"%vel_Ang

			# print "damped angle %f"%theta_Damped


			print "vel x body frame %f"%vel_X_Body_Frame
			print "vel y body frame %f"%vel_Y_Body_Frame

		

		v.goVel(vel_X_Body_Frame, vel_Y_Body_Frame, 0)
	else:
		v.goVel(0,0,0)
		print "Entering go to goal"
		Statics.state = "goToGoal"

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

	if ((Statics.sideOfField == "Away" and ballX < -0.75) or (Statics.sideOfField == "Home" and ballX > 0.75)):
		print "Entering Go To GOAL"
		Statics.state = "goToGoal"

	enemyGoalCenterX = 0
	enemyGoalCenterY = 0
	if (Statics.sideOfField == "Away"):
		enemyGoalCenterX = 1.4
	else:
		enemyGoalCenterX = -1.4
	deltaX = enemyGoalCenterX - ballX
	deltaY = enemyGoalCenterY - ballY

	commanded_X_pos = ballX + ((-0.2)*deltaX/math.sqrt(deltaX*deltaX + deltaY*deltaY)) 
	commanded_Y_pos = ballY + ((-0.2)*deltaY/math.sqrt(deltaX*deltaX + deltaY*deltaY)) 

	# convert to floats
	commanded_X_pos = float(commanded_X_pos)
	commanded_Y_pos = float(commanded_Y_pos)
	commanded_Ang_pos = float(0)
	current_X_pos = float(robotX)
	current_Y_pos = float(robotY)
	current_Ang_pos = float(theta)

	XErr = commanded_X_pos - current_X_pos
	YErr = commanded_Y_pos - current_Y_pos
	# AngleErr = commanded_Ang_pos - current_Ang_pos

	flag = False;

	if (abs(XErr) > 0.1 or abs(YErr) > 0.1):
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

		# vel_Ang = 0
		# error_Ang = 0
		# if (abs(AngleErr) > 0.2):
		# 	error_Max_Ang = 3.14 #in radians
		# 	vel_Max_Ang = 1
		# 	error_Ang = AngleErr
		# 	kp_Ang = float(vel_Max_Ang)/float(error_Max_Ang) # units don't match, but that's okay
		# 	vel_Ang = kp_Ang*error_Ang

		# theta_Damped = theta - vel_Ang/4
		vel_X_Body_Frame = math.cos(theta)*vel_X + math.sin(theta)*vel_Y 
		vel_Y_Body_Frame = -1*(math.cos(theta)*float(vel_Y) - math.sin(theta)*float(vel_X))


		if (debug == 1 and Statics.samples == maxSamples):
			Statics.samples = 0
			print data
			print "error in X %f"%error_X
			print "current_X_pos %f"%current_X_pos
			print "vel X %f"%vel_X
			print
			print "error in Y %f"%error_Y
			print "current_Y_pos %f"%current_Y_pos
			print "vel Y %f"%vel_Y
			# print
			# print "error in angle %f"%(error_Ang*float(180)/float(math.pi))
			# print "current Angle %f"%(current_Ang_pos*float(180)/float(math.pi))
			# print "angle vel %f"%vel_Ang

			# print "damped angle %f"%theta_Damped


			print "vel x body frame %f"%vel_X_Body_Frame
			print "vel y body frame %f"%vel_Y_Body_Frame

		

		v.goVel(vel_X_Body_Frame, vel_Y_Body_Frame, 0)
	else:
		v.goVel(0,0,0)
		Statics.state = "attackEnemy"
		print "Entering Attack Enemy"	

def listener():

	rospy.init_node('listener', anonymous=True)

	# plt.xlabel('time (s)')
	# plt.ylabel('positions (m)')
	# plt.title('confusion')
	# plt.grid(True)
	# X = np.linspace(0,2,1000)
	# Y = X**2 + np.random.random(X.shape)

	# plt.ion()
	# Statics.graph = plt.plot(X,Y)[0]

	rospy.Subscriber('Vision', String, callback)
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
	# SetM2pidq(128,65536,32768,16384,243759)
	# SetM2pidq(129,65536,32768,16384,264568)
	# SetM1pidq(129,65536,32768,16384,256704)
	p = int(65536 * 4) #262144
	i = int(65536 * 2) #131072
	d = int(65536 * 6)  #65536
	SetM1pidq(129,p,i,d,158372)
	SetM2pidq(128,p,i,d,164501)
	SetM2pidq(129,p,i,d,141356)

	listener()
