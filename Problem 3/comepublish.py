#!/usr/bin/env python
#commit message
import rospy
from my_package.msg import bot_pose  # <-- Fix package name here

def command_publisher():
    pub = rospy.Publisher('bot_commands', bot_pose, queue_size=10)
    rospy.init_node('command_publisher', anonymous=True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        command = input("Enter command (forward, left, right, back): ")
        pose_msg = bot_pose()
        pose_msg.command = command
        pose_msg.x = 0.0  # <-- Add missing fields
        pose_msg.y = 0.0
        pose_msg.theta = 0.0
        pub.publish(pose_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        command_publisher()
    except rospy.ROSInterruptException:
        pass
