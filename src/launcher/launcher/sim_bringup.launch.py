from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([

        Node(
            package='vision',
            executable='camera_node',
            name='camera_node',
            output='screen'
        ),

        Node(
            package='power_monitor',
            executable='power_node',
            name='power_node',
            output='screen'
        ),

        Node(
           package='sensor_pkg',
           executable='gps_dummy_node',   # atau nama node di sensor_pkg kamu
           name='gps_dummy_node',
           output='screen'
        )
    ])