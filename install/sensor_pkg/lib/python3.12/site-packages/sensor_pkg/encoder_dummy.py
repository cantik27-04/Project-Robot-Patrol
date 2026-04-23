import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class EncoderDummy(Node):
    def __init__(self):
        super().__init__('encoder_dummy')
        self.publisher_ = self.create_publisher(Int32, '/sensor/encoder', 10)
        self.timer = self.create_timer(1.0, self.publish_data)

    def publish_data(self):
        msg = Int32()
        msg.data = random.randint(0, 100)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Encoder: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = EncoderDummy()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
