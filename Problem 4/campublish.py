#!/usr/bin/env python3
#new
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np

class CameraPublisher:
    def __init__(self):
        rospy.init_node('camera_publisher', anonymous=True)
        self.publisher = rospy.Publisher('camera_image', Image, queue_size=10)
        self.bridge = CvBridge()
        self.rate = rospy.Rate(30)  # 30 Hz

        # Camera setup
        self.camera = cv2.VideoCapture(0)  # 0 for default camera

        if not self.camera.isOpened():
            rospy.logerr("Could not open camera")
            rospy.signal_shutdown("Could not open camera")
            return

    def run(self):
        while not rospy.is_shutdown():
            ret, frame = self.camera.read()
            if not ret:
                rospy.logwarn("Could not read frame")
                break

            # Task 2: Edge detection
            edges = cv2.Canny(frame, 100, 200)
            # Convert edges to BGR format for displaying
            frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

            # Publish the image
            try:
                self.publisher.publish(self.bridge.cv2_to_imgmsg(frame, "bgr8"))
                rospy.loginfo("Publishing camera frame")
            except Exception as e:
                rospy.logerr("Error publishing image: %s", str(e))

            self.rate.sleep()

        self.camera.release()

if __name__ == '__main__':
    try:
        camera_publisher = CameraPublisher()
        camera_publisher.run()
    except rospy.ROSInterruptException:
        pass
