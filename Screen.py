import cv2

from Recognizer import *
from Features.Clock import *

class Screen:
    def __init__(self):
        # Define sceen variables
        self.HUDText = (255,200,0)
        self.HUDColor = (207,172,50)
        self.font = cv2.FONT_HERSHEY_DUPLEX
        self.startTime = 0 

        self.useRecognizer = False
        self.recognizer = Recognizer()

        self.features = [
            Clock()
        ]
 
    def onStep(self):
        for feature in self.features:
            feature.onStep()

    def redrawAll(self, img):
        if self.useRecognizer:
            cv2.putText(img, "Processing...", (10, 115), self.font, 0.5, self.HUDText, 2)
            self.recognizer.showFaces(img)
        
        # Add Features to our screen
        for feature in self.features:
            feature.redraw()

        # Display our image
        cv2.imshow('HUD', img)


    def keyPress(self, k):
        # F1 key toggles if we're using the recognizer
        if k == 190: 
            self.useRecognizer = not self.useRecognizer