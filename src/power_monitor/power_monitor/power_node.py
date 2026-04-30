import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class PowerMonitor(Node):
    def __init__(self):
        super().__init__('power_monitor')

        self.pub_voltage = self.create_publisher(Float32, '/battery_voltage', 10)
        self.timer = self.create_timer(1.0, self.publish_data)

    def publish_data(self):
        msg = Float32()
        msg.data = random.uniform(11.5, 12.6)

        self.pub_voltage.publish(msg)
        self.get_logger().info(f'Battery: {msg.data:.2f} V')


def main():
    rclpy.init()
    node = PowerMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
