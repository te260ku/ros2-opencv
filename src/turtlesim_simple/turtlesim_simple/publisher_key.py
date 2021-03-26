import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys, select, termios, tty

settings = termios.tcgetattr(sys.stdin)

moveBindings = {
		'a':(0.0,0.0,0.0,0.0,0.0,0.1),
		's':(0.1,0.0,0.0,0.0,0.0,0.1),
		'd':(0.2,0.0,0.0,0.0,0.0,0.1),
		'f':(0.3,0.0,0.0,0.0,0.0,0.1),
		'default':(1.0, 0.0 ,0.0 ,0.0, 0.0, 0.1)
}

class KeyPublisher(Node):
	def __init__(self):
		super().__init__('key_publisher')
		self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
		self.timer = self.create_timer(0.5, self.timer_callback)

	def timer_callback(self):
		msg = Twist()
		key = input()
		if key in moveBindings.keys():
			msg.linear.x = moveBindings[key][0]
			msg.linear.y = moveBindings[key][1]
			msg.linear.z = moveBindings[key][2]
			msg.angular.x = moveBindings[key][3]
			msg.angular.y = moveBindings[key][4]
			msg.angular.z = moveBindings[key][5]
		else:
			msg.linear.x = moveBindings['default'][0]
			msg.linear.y = moveBindings['default'][1]
			msg.linear.z = moveBindings['default'][2]
			msg.angular.x = moveBindings['default'][3]
			msg.angular.y = moveBindings['default'][4]
			msg.angular.z = moveBindings['default'][5]

		self.pub.publish(msg)


def main(args=None):
	rclpy.init(args=args)
	key_publisher = KeyPublisher()
	rclpy.spin(key_publisher)

	key_publisher.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
	main()
