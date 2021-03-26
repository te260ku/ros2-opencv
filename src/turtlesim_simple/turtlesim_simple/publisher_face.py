import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import cv2
import sys, select, termios, tty

face_cascade = cv2.CascadeClassifier('/usr/local/lib/python3.8/dist-packages/cv2/data/haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)

global detected
detected = False

class KeyPublisher(Node):
	def __init__(self):
		super().__init__('key_publisher')
		self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
		self.timer = self.create_timer(0.5, self.timer_callback)

	def timer_callback(self):
		msg = Twist()

		ret, img = cap.read()
		img = cv2.resize(img, (int(img.shape[1]*0.7), int(img.shape[0]*0.7)))
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

		if len(faces) > 0:
			msg.angular.z = 0.1
			print("detected")

		self.pub.publish(msg)


def main(args=None):
	rclpy.init(args=args)
	key_publisher = KeyPublisher()
	rclpy.spin(key_publisher)

	cap.release()
	cv2.destroyAllWindows()
	key_publisher.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
	main()
