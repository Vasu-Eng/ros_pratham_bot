#! /usr/bin/env python3
import rospy , cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge , CvBridgeError

def img_clbck(img_msg):
    try:
        bridge = CvBridge()
        frame = bridge.imgmsg_to_cv2(img_msg,desired_encoding="passthrough")
        cv2.imshow("Image",frame)
        if cv2.waitKey(10) & 0xff==27:
            cv2.destroyAllWindows()
    except CvBridgeError as e:
        print(e)

def main():
    rospy.init_node("perception_subscriber")
    rospy.Subscriber("/image",Image,img_clbck)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Error:",str(e))
    finally:
        print("Executed Subscriber")

