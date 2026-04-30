from setuptools import setup

package_name = 'launcher'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],  # WAJIB ADA
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/launcher']),
    ('share/launcher', ['package.xml']),
    ('share/launcher/launch', ['launcher/sim_bringup.launch.py']),
  ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='asracantik',
    maintainer_email='asrabelajar@gmail.com',
    description='ROS2 launcher for simulation system',
    license='MIT',
)