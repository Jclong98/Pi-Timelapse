import time

from picamera import PiCamera

camera = PiCamera()
# camera.resolution = (1024, 768)
# camera.rotation = 180


from datetime import datetime

def take_picture(path):
    print(f"{datetime.now()}: {path}")
    
    # Camera warm-up time
    camera.start_preview()
    time.sleep(1)

    camera.capture(path)