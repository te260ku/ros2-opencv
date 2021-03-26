import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class SimplePublisher(Node):
	def __init__(self):
		super().__init__('simple_publisher')
		self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
		timer_period = 0.5
		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.i = 0
	def timer_callback(self):
		msg = Twist()
		msg.linear.x = 0.2
		msg.linear.y = 0.1
		msg.linear.z = 0.0
		msg.angular.x = 0.0
		msg.angular.y = 0.0
		msg.angular.z = 2.0
		self.publisher_.publish(msg)
		self.get_logger().info('Publishing: linear(%f, %f, %f), angular(%f, %f, %f)' % (msg.linear.x, msg.linear.y, msg.linear.z, msg.angular.x, msg.angular.y, msg.angular.z))

def main(args=None):
	rclpy.init(args=args)
	simple_publisher = SimplePublisher()
	rclpy.spin(simple_publisher)
	simple_publisher.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
	main()
