
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

if __name__ == '__main__':
	SetM2pidq(128,65536,32768,16384,243759)
	SetM2pidq(129,65536,32768,16384,264568)
	SetM1pidq(129,65536,32768,16384,256704)
	v.myCircle()
	v.mySquare()
    listener()
