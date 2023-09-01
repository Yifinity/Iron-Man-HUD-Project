import os
import numpy as np
from PIL import Image

from Screen import *
from Camera import *

from Scenes.RunScene import *


class App:
    def __init__(self):
        # Create our objects to run 
        self.userCamera = Camera(self)
        self.userScreen = Screen(self)

        self.scenes = [
            RunScene(self)
        ]

        self.currentScene = self.scenes[0]

    def onStep(self):
        self.currentScene.onStep()

    def redrawAll(self):
        self.currentScene.redrawAll()
    
    def onKeyPress(self):
        k = cv2.waitKey(1)
        if k == 27:
            self.userCamera.terminateStream()
            exit()
        else:
            self.userScreen.keyPress(k)