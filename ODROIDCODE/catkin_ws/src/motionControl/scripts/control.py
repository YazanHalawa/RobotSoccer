




#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import velchange as v
from roboclaw import *

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('vision', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()




def seek(current_X_pos):
  #move kp and other calculations to param file to only be done once
  # if (current_X_pos - old_X_pos > .5):
  #   flag = True

  # if flag: 
    # error_Max_X = 5
    # vel_Max_X = 1
    # error_X = commanded_X_pos - current_X_pos
    # kp_X = vel_Max_X/error_Max_X # units don't match, but that's okay
    # vel_X = kp_X*error_X

    # error_Max_Y = 5
    # vel_Max_Y = 1
    # error_Y = commanded_Y_pos - current_Y_pos
    # kp_Y = vel_Max_Y/error_Max_Y # units don't match, but that's okay
    # vel_Y = kp_Y*error_Y

    # error_Max_Ang = 3.14 #in radians
    # vel_Max_Ang = 3
    # error_Ang = commanded_Ang_pos - current_Ang_pos
    # kp_Ang = vel_Max_Ang/error_Max_Ang # units don't match, but that's okay
    # vel_Ang = kp_Ang*error_Ang

  commanded_X_pos = 0

  error_Max_X = 5
  vel_Max_X = 1
  error_X = commanded_X_pos - current_X_pos
  kp_X = vel_Max_X/error_Max_X # units don't match, but that's okay
  vel_X = kp_X*error_X

  commanded_Y_pos = 0
  current_Y_pos = 0

  error_Max_Y = 5
  vel_Max_Y = 1
  error_Y = commanded_Y_pos - current_Y_pos
  kp_Y = vel_Max_Y/error_Max_Y # units don't match, but that's okay
  vel_Y = kp_Y*error_Y

  commanded_Ang_pos = 0
  current_Ang_pos = 0

  error_Max_Ang = 3.14 #in radians
  vel_Max_Ang = 3
  error_Ang = commanded_Ang_pos - current_Ang_pos
  kp_Ang = vel_Max_Ang/error_Max_Ang # units don't match, but that's okay
  vel_Ang = kp_Ang*error_Ang

  print "vel x is%d"%vel_X

  v.goVel(vel_X,vel_Y,vel_Ang)

  if (current_X_pos != 0):
    current_X_pos = current_X_pos - .01





if __name__ == '__main__':
  current_X_pos = 10;
  while True:
    seek(current_X_pos)
    #listener()






