import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class EncoderDummy(Node):
    def __init__(self):
        super().__init__('encoder_dummy')

        self.publisher_ = self.create_publisher(Int32, '/sensor/encoder', 10)

        # nilai awal encoder
        self.encoder_value = 0

        # 10 Hz biar terasa real-time (0.1 detik)
        self.timer = self.create_timer(0.1, self.publish_data)

    def publish_data(self):
        msg = Int32()

        # simulasi robot bergerak maju terus
        self.encoder_value += random.randint(1, 5)

        # sedikit noise biar realistis
        if random.random() < 0.1:
            self.encoder_value += random.randint(-2, 2)

        msg.data = self.encoder_value

        self.publisher_.publish(msg)

        self.get_logger().info(f'Encoder LIVE: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = EncoderDummy()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
