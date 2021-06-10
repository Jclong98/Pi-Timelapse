import os, time
from datetime import datetime

# from picamera import PiCamera

# camera = PiCamera()
# camera.resolution = (1024, 768)
# camera.rotation = 180


def take_picture(directory):
    filepath = f"{os.path.join(directory, str(time.time()))}.jpg"
    print(f"{datetime.now()}: {filepath}")
    
    # Camera warm-up time
    # camera.start_preview()
    time.sleep(1)

    # camera.capture(filepath)

if __name__ == "__main__":
    take_picture('./')