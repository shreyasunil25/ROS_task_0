#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def number_publisher():
    pub = rospy.Publisher('multiples_of_two', Int32, queue_size=10)
    rospy.init_node('number_publisher', anonymous=True)
    rate = rospy.Rate(1) # 1 Hz
    number = 2
    while not rospy.is_shutdown():
        rospy.loginfo("Publishing: %s", number)
        pub.publish(number)
        number *= 2
        rate.sleep()

if __name__ == '__main__':
    try:
        number_publisher()
    except rospy.ROSInterruptException:
        pass
