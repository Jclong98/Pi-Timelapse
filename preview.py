#!/usr/bin/env python3

from picamera import PiCamera
from time import sleep

camera = PiCamera()
# camera.resolution = (1024, 768)
camera.rotation = 0
camera.start_preview()
sleep(300)