import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer


class BatterySubscriber(Node):
    def __init__(self):
        super().__init__('battery_gui_node')
        self.voltage = 0.0

        self.create_subscription(
            Float32,
            '/battery_voltage',
            self.callback,
            10
        )

    def callback(self, msg):
        self.voltage = msg.data


class Dashboard(QWidget):
    def __init__(self, node):
        super().__init__()

        self.node = node

        self.setWindowTitle("Robot Dashboard")
        self.setGeometry(400, 200, 300, 150)

        self.label = QLabel("Battery: -- V")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_ui)
        self.timer.start(500)

    def update_ui(self):
        v = self.node.voltage
        self.label.setText(f"Battery: {v:.2f} V")

        if v < 11.8:
            self.label.setStyleSheet("color: red; font-size: 20px;")
        else:
            self.label.setStyleSheet("color: green; font-size: 20px;")


def main():
    rclpy.init()

    node = BatterySubscriber()

    app = QApplication(sys.argv)
    gui = Dashboard(node)
    gui.show()

    import threading
    t = threading.Thread(target=rclpy.spin, args=(node,), daemon=True)
    t.start()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
