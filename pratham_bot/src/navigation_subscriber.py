#!/usr/bin/env python3

# publisher command :-
# rosrun teleop_twist_keyboard teleop_twist_keyboard.py _speed:=100 _turn:=100 cmd_vel:=/navigation/cmd_vel
#sudo chown root.gpio /dev/gpiomem
import rospy
from motor_drivers_interface import motor_driver 
from geometry_msgs.msg import Twist
# Initialize the node with rospy

def callback(msg):
    print(f" linear_X : {msg.linear.x} \n angular_z : {msg.angular.z}")
    take_action(msg.linear.x,msg.angular.z)

def take_action(X,Z):
    
    if X == 0 and Z == 0 :
        motor_driver.stop()
    elif X > 0 and Z == 0 :
        motor_driver.farward(X)
    elif X < 0 and Z == 0 :
        motor_driver.backward(-X)
    elif X == 0 and Z < 0 :
        motor_driver.right(-Z)
    elif X == 0 and Z > 0 :
        motor_driver.left(Z)
    elif X > 0 and Z < 0 :
        motor_driver.turn_right(X,-Z)
    elif X > 0 and Z > 0 :
        motor_driver.turn_left(X,Z)
    elif X < 0 and Z > 0 :
        motor_driver.turn_bacward_right(-X,Z)
    elif X < 0 and Z < 0 :
        motor_driver.turn_backward_left(-X,-Z)

def main():
    rospy.init_node('navigation_subscriber')
    rospy.Subscriber("/navigation/cmd_vel",Twist,callback)
    rospy.spin()


if __name__ == '__main__':
    main()

