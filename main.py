import os
import numpy as np
from PIL import Image

from Screen import *
from Camera import *

def main():
    # Create our objects to run 
    userCamera = Camera()
    userScreen = Screen()

    while(True):
        frame = userCamera.getFrame()
        userScreen.onStep()
        userScreen.redrawAll(frame)

        # Check if user presses ESC to exit loop
        k = cv2.waitKey(1)
        if k == 27:
            break
    
        else:
            userScreen.keyPress(k)
    
    # Outside the loop, we've ended the stream. 
    userCamera.terminateStream()
    exit()

main()
