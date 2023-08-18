# Camera class - reads images and sends them to recognizer/screen
import cv2
import time
from datetime import datetime

class Camera:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.cam.set(cv2.CAP_PROP_FPS, 30)

        self.cam.set(3, vidWidth) # set video width
        self.cam.set(4, vidHeight) # set video height
        pass

    def onStep(self):
        pass

    def redrawAll(self):
        pass




