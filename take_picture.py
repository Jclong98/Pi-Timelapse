import os, time
from datetime import datetime

from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1920, 1080)
# camera.rotation = 180


def take_picture(path):
    print(f"{datetime.now()}: {path}")
    
    # Camera warm-up time
    camera.start_preview()
    time.sleep(2)

    camera.capture(path)

if __name__ == "__main__":
    take_picture('./pic.jpg')