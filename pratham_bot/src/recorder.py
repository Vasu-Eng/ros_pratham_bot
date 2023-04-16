#!/usr/bin/env python3
import rospy
from std_msgs.msg import Bool, Float32
from sensor_msgs.msg import CompressedImage,Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import sys
from select import select
import termios
import tty
import numpy as np
import os

bridge = CvBridge()
Key =  ""
counter = 0
t = False #toggle var

filename = 'video.avi'
frames_per_second = 24.0
res = '720p'

# Set resolution for the video capture
# Function adapted from https://kirr.co/0l6qmh
def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)


# Standard Video Dimensions Sizes
STD_DIMENSIONS =  {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

# grab resolution dimensions and set video capture to it.
def get_dims(cap, res='1080p'):
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]
    ## change the current caputre device
    ## to the resulting resolution
    change_res(cap, width, height)
    return width, height

# Video Encoding, might require additional installs
# Types of Codes: http://www.fourcc.org/codecs.php
VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}


def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
      return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['mp4']

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

def callback(msg):
    global Key,counter,t


    # out = cv2.VideoWriter(filename ,cv2.VideoWriter_fourcc(*'XVID') , 30, (1080,1920))
    if Key == "p":
        try:
            # Convert your ROS Image message to OpenCV2
            cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
        except CvBridgeError as e:
            print(e)
        counter = counter + 1
        Key = ""
        print("Received an image!")
        # Save your OpenCV2 image as a jpeg 
        cv2.imwrite(f'camera_image{counter}.jpeg', cv2_img)
    # if Key == "r":
    #         if t is False :
    #             print("start video recording")
    #             Key = "temp"
    #             t = True
    #         elif t is True :
    #             out.release()
    #             print("End video recording !! ")
    #             Key = ""  
    #             t = False
    # if Key =="temp":
    #         out.write(cv2_img)   

def main(): #working
    global Key
    rospy.init_node("image_publisher", anonymous= False)
    rospy.Subscriber("/image",Image,callback)
    rate = rospy.Rate(10)
    settings = termios.tcgetattr(sys.stdin)
    try:
        while not rospy.is_shutdown():
            Key = getKey(settings,None)
            if (Key == '\x03'):
                break
    except Exception as e:
        print(e)

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN,settings)

if __name__ == '__main__':
        try:
            main()
            # stream_compressed_image()

        except rospy.ROSInterruptException:
            pass




