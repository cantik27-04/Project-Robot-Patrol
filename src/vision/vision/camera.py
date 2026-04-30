import rclpy
from rclpy.node import Node
import cv2


class CameraNode(Node):

    def __init__(self):
        super().__init__('camera_node')

        # ambil kamera (coba 0 dulu, kalau gagal ganti 1)
        self.cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

        if not self.cap.isOpened():
            self.get_logger().error("Camera tidak bisa dibuka!")
        else:
            self.get_logger().info("Camera berhasil dibuka")

        # loop ROS2 (30 FPS)
        self.timer = self.create_timer(0.03, self.timer_callback)

    def timer_callback(self):
        ret, frame = self.cap.read()

        if not ret:
            self.get_logger().warn("Frame tidak terbaca")
            return

        # tampilkan frame
        cv2.imshow("ROS2 Camera", frame)

        # WAJIB supaya window OpenCV update
        cv2.waitKey(1)

    def destroy_node(self):
        self.cap.release()
        cv2.destroyAllWindows()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = CameraNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
