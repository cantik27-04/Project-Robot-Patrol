from dummy_ultrasonic import get_distance
from dummy_bumper import get_bumper
from dummy_camera import get_camera
import time

while True:
    distance = get_distance()
    bumper = get_bumper()
    camera = get_camera()

    print("Distance:", distance, "cm")
    print("Bumper:", bumper)
    print("Camera:", camera)

    # LOGIKA ROBOT
    if bumper == 0:
        print("🚨 TABRAKAN! STOP!")
    elif camera == "person":
        print("👤 ADA ORANG! HATI-HATI!")
    elif distance < 30:
        print("⚠️ HALANGAN DEKAT!")
    else:
        print("✅ AMAN JALAN")

    print("----------------------")

    time.sleep(1)