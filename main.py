from simulation.dummy_ultrasonic import read_ultrasonic
from simulation.dummy_bumper import read_bumper
from simulation.dummy_gnss import read_gnss
from simulation.dummy_camera import capture_frame

import time

while True:

    distance = read_ultrasonic()
    bumper = read_bumper()
    lat, lon = read_gnss()
    frame = capture_frame()

    print("Ultrasonic:", distance, "cm")
    print("Bumper:", bumper)
    print("GPS:", lat, lon)
    print("Camera:", frame)

    print("----------------------")

    time.sleep(2)