# Camera class - reads images and sends them to recognizer/screen
import cv2
import time
from datetime import datetime

class Camera:
    def __init__(self, app):
        # Get our app instance
        self.app = app
        self.vidWidth = 800
        self.vidHeight = 480

        self.cam = cv2.VideoCapture(0)
        self.cam.set(cv2.CAP_PROP_FPS, 45)

        self.cam.set(3, self.vidWidth) # set video width
        self.cam.set(4, self.vidHeight) # set video height

    def getFrame(self):
        # Get us our next image
        ret, img = self.cam.read()
        return img

    def redrawAll(self):
        pass

    def terminateStream(self):
        self.cam.release()
        cv2.destroyAllWindows()




