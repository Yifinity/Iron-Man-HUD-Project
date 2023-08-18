import os
import numpy as np
from PIL import Image
import math

from Screen import *
from Camera import *

def main():
    # Create our objects to run 
    userCamera = Camera()
    userScreen = Screen()


    while(True):
        
        ret, img = cam.read()
        
        cv2.imshow('HUD', img)
        
        # Check if user presses ESC to exit loop
        k = cv2.waitKey(1)

        if k == 27:
            break

    cam.release()
    cv2.destroyAllWindows()
    exit()

main()
