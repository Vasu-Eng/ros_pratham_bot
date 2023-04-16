#! /usr/bin/env python3
import rospy 
from std_msgs.msg import String

rospy.init_node('send_data')

publisher = rospy.Publisher("/data/send",String, queue_size=1) # enter topic and type accordingly


def callback(event):
	msg = String()
	msg.data = "Paarth" # type data here
	publisher.publish(msg)

pub_period = rospy.get_param("~pub_period",1.0)

rospy.Timer(rospy.Duration.from_sec(pub_period),callback)

rospy.spin()
