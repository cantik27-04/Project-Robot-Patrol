import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class GPSDummy(Node):
    def __init__(self):
        super().__init__('gps_dummy')
        self.publisher_ = self.create_publisher(String, '/sensor/gps', 10)
        self.timer = self.create_timer(1.0, self.publish_data)

        # posisi awal
        self.lat = -7.5
        self.lon = 112.7

    def publish_data(self):
        # simulasi bergerak
        self.lat += 0.0001
        self.lon += 0.0001

        msg = String()
        msg.data = f"Lat:{self.lat}, Lon:{self.lon}"

        self.publisher_.publish(msg)
        self.get_logger().info(msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = GPSDummy()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
