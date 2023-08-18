import cv2
import time
from datetime import datetime

class Screen:
    def __init__(self):
        # Define sceen variables
        self.HUDText = (255,200,0)
        self.HUDColor = (207,172,50)
        self.font = cv2.FONT_HERSHEY_DUPLEX
        self.startTime = 0 

    def onStep(self):
        self.now = datetime.now() # Current Date and Time.
        # Format time 
        self.date_time = self.now.strftime("%m/%d/%Y, %H:%M:%S")

        self.timeNow = time.time()
        self.fps = 1 / (self.timeNow - self.startTime)
        self.startTime = self.timeNow

    def redrawAll(self, img):
        # Show the next image displayed
        cv2.imshow('HUD', img)
        cv2.putText(img, "Mk7", (10, 50), self.font, 2, self.HUDText, 2)
        cv2.putText(img, ("Date: " + self.date_time), (10,75), self.font, 0.5,
                     self.HUDText,1)       
        cv2.putText(img, ("FPS: "+ str(self.math.floor(self.fps))), (10, 95),
                     self.font, 0.5, self.HUDText, 1)      
