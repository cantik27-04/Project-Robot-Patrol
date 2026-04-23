import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')

        self.publisher_ = self.create_publisher(Image, 'image_raw', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)

        self.cap = cv2.VideoCapture(0)

        # optional tuning biar stabil
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        self.bridge = CvBridge()

        self.get_logger().info("Camera Node Started")

    def timer_callback(self):
        ret, frame = self.cap.read()

        if ret:
            # Menampilkan jendela gambar langsung dari OpenCV
            cv2.imshow("Camera View", frame)
            cv2.waitKey(1) # Penting: Memberi waktu OpenCV untuk merender gambar
            msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
            self.publisher_.publish(msg)
            self.get_logger().info("Publishing frame...")
        else:
            self.get_logger().warn("Failed to read frame")

def main(args=None):
    rclpy.init(args=args)
    node = CameraNode()
    rclpy.spin(node)

    node.cap.release()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()