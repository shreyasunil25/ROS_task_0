#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class ImageSubscriber:
    def __init__(self):
        rospy.init_node('image_subscriber', anonymous=True)
        self.subscriber = rospy.Subscriber('camera_image', Image, self.callback)
        self.bridge = CvBridge()

    def callback(self, data):
        try:
            # Convert ROS Image message to OpenCV image
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except Exception as e:
            rospy.logerr("Error converting image: %s", str(e))
            return

        # Display the image
        cv2.imshow("Camera Feed", cv_image)
        cv2.waitKey(1)  # 1 millisecond delay

    def run(self):
        rospy.spin()  # Keep the node running

if __name__ == '__main__':
    try:
        image_subscriber = ImageSubscriber()
        image_subscriber.run()
    except rospy.ROSInterruptException:
        pass
