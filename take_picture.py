from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
# camera.rotation = 180

from datetime import datetime

def take_picture(path):
    print(f"{datetime.now()}: {path}")
    camera.capture(path)