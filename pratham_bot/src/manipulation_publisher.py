#!/usr/bin/env python3
import rospy
from std_msgs.msg import UInt16MultiArray
import sys
from select import select
import termios
import tty
# Initialize the node with rospy
#sudo chmod 666 /dev/ttyUSB0 
pose_tilt = 96
pose_pan = 96

def getKey(settings,timeout):
        
    tty.setraw(sys.stdin.fileno())
    # sys.stdin.read() returns a string on Linux
    rlist, _, _ = select([sys.stdin], [], [], timeout)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN,settings)
    return key

def main():
    global pose_pan,pose_tilt
    rospy.init_node('manipulation_publisher')
    publisher = rospy.Publisher("/manipulation/servo_ctl",UInt16MultiArray,queue_size=10)
    rospy.rate = 10
    msg = UInt16MultiArray()
    settings = termios.tcgetattr(sys.stdin)
    try:
        while(1):
            key = getKey(settings,None)
            # print(key)
            msg.data = [pose_pan,pose_tilt]
            publisher.publish(msg)

            if key == "t":
                if pose_tilt > 0:
                    pose_tilt = pose_tilt - 1
                else :
                    pose_tilt = 0
            elif key == "g":
                if pose_tilt < 180 :
                    pose_tilt = pose_tilt + 1
                else :
                    pose_tilt = 180
            elif key == "f":
                if pose_pan < 180:
                    pose_pan = pose_pan + 1
                else :
                    pose_pan = 180
            elif key == "h":
                if pose_pan > 0:
                    pose_pan = pose_pan - 1
                else :
                    pose_pan = 0
            elif key == "b":
                pose_pan = 96
                pose_tilt = 96
            if (key == '\x03'):
                break
    except Exception as e:
        print(e)

    finally:
        # pub_thread.stop()
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN,settings)
        

if __name__ == '__main__':
        try:
            main()
        except rospy.ROSInterruptException:
            pass
 