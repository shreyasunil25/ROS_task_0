#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(data):
    added_value = data.data + 5
    rospy.loginfo("Added 5: %s", added_value)

def adder():
    rospy.init_node('adder', anonymous=True)
    rospy.Subscriber('multiplied_by_ten', Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    adder()
