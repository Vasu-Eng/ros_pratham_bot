#!/usr/bin/env python3
import rospy
from hardware_interface import led
from std_msgs.msg import String
# Initialize the node with rospy

def callback(msg):
    global button_status
    button_status = msg.data
    #print(f"button_status : {button_status}")
    if button_status == "on":
          print("LED : ON")
           led.ON()
    elif button_status == "off":
           print("LED : OFF")
          led.OFF()

def main():
    rospy.init_node('led_subscriber')
    rospy.Subscriber("/led/control",String,callback)
    rospy.spin()


if __name__ == '__main__':
    main()
