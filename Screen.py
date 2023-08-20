import cv2
import time
import math
from datetime import datetime

from Recognizer import *

class Screen:
    def __init__(self):
        # Define sceen variables
        self.HUDText = (255,200,0)
        self.HUDColor = (207,172,50)
        self.font = cv2.FONT_HERSHEY_DUPLEX
        self.startTime = 0 

        self.useRecognizer = False
        self.recognizer = Recognizer()

    def onStep(self):
        self.now = datetime.now() # Current Date and Time.
        # Format time 
        self.date_time = self.now.strftime("%B %d, %Y | %I:%M%p")

        # FPS Calculation
        self.timeNow = time.time()
        self.fps = 1 / (self.timeNow - self.startTime)
        self.startTime = self.timeNow

    def redrawAll(self, img):
        if self.useRecognizer:
            self.recognizer.showFaces(img)

        # Show the next image displayed
        cv2.putText(img, "Mk7", (10, 50), self.font, 2, self.HUDText, 2)
        cv2.putText(img, (self.date_time), (10,75), self.font, 0.5,
                     self.HUDText,1)       
        cv2.putText(img, ("FPS: "+ str(math.floor(self.fps))), (10, 95),
                     self.font, 0.5, self.HUDText, 1)      
        cv2.imshow('HUD', img)

    def keyPress(self, k):
        # F1 key toggles if we're using the recognizer
        if k == 112: 
            self.useRecognizer = not self.useRecognizer