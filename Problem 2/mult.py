#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(data):
    multiplied_value = data.data * 10
    pub.publish(multiplied_value)
    rospy.loginfo("Multiplied by 10: %s", multiplied_value)

def multiplier():
    rospy.init_node('multiplier', anonymous=True)
    global pub
    pub = rospy.Publisher('multiplied_by_ten', Int32, queue_size=10)
    rospy.Subscriber('multiples_of_two', Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    multiplier()
