import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
import random

class GNSSDummy(Node):
    def __init__(self):
        super().__init__('gnss_dummy')

        # publisher (sama gaya seperti encoder kamu)
        self.publisher_ = self.create_publisher(NavSatFix, '/gps_data', 10)

        # posisi awal (dummy location)
        self.lat = 1.135000
        self.lon = 104.030000

        # timer realtime (0.5 detik = 2 Hz)
        self.timer = self.create_timer(0.5, self.publish_data)

    def publish_data(self):
        msg = NavSatFix()

        # simulasi pergerakan kecil (biar real-time feel)
        self.lat += random.uniform(-0.00001, 0.00001)
        self.lon += random.uniform(-0.00001, 0.00001)

        msg.latitude = self.lat
        msg.longitude = self.lon
        msg.altitude = 10.0

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'GPS LIVE -> lat: {self.lat:.6f}, lon: {self.lon:.6f}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = GNSSDummy()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
