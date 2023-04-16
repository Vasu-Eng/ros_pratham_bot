#!/usr/bin/env python3
import rospy
from servo_drivers_interface import servo_driver
from std_msgs.msg import Float32MultiArray
# Initialize the node with rospy

def callback(msg):
   pose_pan = msg.data[0]
   pose_tilt = msg.data[1]
   servo_driver.writeServo(pose_pan,pose_tilt)

def main():
    rospy.init_node('manipulation_subscriber')
    rospy.Subscriber("/manipulation/servo_ctl",Float32MultiArray,callback)
    rospy.spin()


if __name__ == '__main__':
    main()
