#!/usr/bin/env python3
import rospy
from hardware_interface import button
from std_msgs.msg import String
# Initialize the node with rospy

def main():
    rospy.init_node('button_piblisher')
    publisher = rospy.Publisher("/led/control",String,queue_size=10)
    rospy.rate = 10
    msg = String()
    while not rospy.is_shutdown():
        msg.data = button.button_status()
        publisher.publish(msg)
        rospy.sleep(0.1)


if __name__ == '__main__':
    main()