import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/asracantik/patrol_robot_system/install/sensor_pkg'
