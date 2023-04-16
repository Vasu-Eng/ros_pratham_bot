#!/usr/bin/env python3
import rospy
from hardware_interface import led
from std_msgs.msg import String
# Initialize the node with rospy

def callback(msg):
    global recieved_data
    recieved_data = msg.data
    print(f"data_recieved : {recieved_data}")


def main():
    rospy.init_node('reciever')
    rospy.Subscriber("~topic",String,callback) # enter topic accordingly & type
    rospy.spin()


if __name__ == '__main__':
    main()
