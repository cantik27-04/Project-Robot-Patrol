import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

class TrackingNode(Node):
    def __init__(self):
        super().__init__('tracking_node')

        # publisher ke robot
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

        # subscriber dari vision
        self.subscription = self.create_subscription(
            Float32,
            '/target_x',
            self.callback_target,
            10
        )

        self.target_x = 0.5  # default tengah

        # loop control
        self.timer = self.create_timer(0.5, self.move_robot)

    def callback_target(self, msg):
        self.target_x = msg.data

    def move_robot(self):
        msg = Twist()

        # hitung error dari tengah (0.5)
        error = self.target_x - 0.5

        msg.linear.x = 0.3
        msg.angular.z = -error  # belok sesuai target

        self.publisher_.publish(msg)

        self.get_logger().info(f"Tracking target: {self.target_x:.2f}")

def main(args=None):
    rclpy.init(args=args)
    node = TrackingNode()
    rclpy.spin(node)
    rclpy.shutdown()
