import os
import numpy as np
from PIL import Image

from Screen import *
from Camera import *


class App:
    def __init__(self):
        # Create our objects to run 
        self.userCamera = Camera(self)
        self.userScreen = Screen(self)

    def onStep(self):
        self.userScreen.onStep()

    def redrawAll(self):
        frame = self.userCamera.getFrame()
        self.userScreen.redrawAll(frame)
    
    def onKeyPress(self):
        k = cv2.waitKey(1)
        if k == 27:
            self.userCamera.terminateStream()
            exit()
        else:
            self.userScreen.keyPress(k)