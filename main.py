import cv2
import os
import numpy as np
from PIL import Image
import math
import time
from datetime import datetime

vidWidth = 800
vidHeight = 480

HUDText = (255,200,0)
HUDColor = (207,172,50)

font = cv2.FONT_HERSHEY_DUPLEX

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 30) #Change to 30
startTime = 0 

cam.set(3, vidWidth) # set video width
cam.set(4, vidHeight) # set video height


while(True):
    now = datetime.now() # Current Date and Time.
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    ret, img = cam.read()
    timeNow = time.time()
    fps = 1 / (timeNow - startTime)
    startTime = timeNow
    cv2.putText(img, "Mk7", (10, 50), font, 2, HUDText, 2)
    cv2.putText(img, ("Date: " + date_time), (10,75), font, 0.5, HUDText,1)       
    cv2.putText(img, ("FPS: "+ str(math.floor(fps))), (10, 95), font, 0.5, HUDText,1)      
    
    cv2.imshow('HUD', img)
    
    k = cv2.waitKey(1) # Press 'ESC' for exiting video \\ Is 5 ms the delay?
    if k == 27:
        break
    elif k==32:
        cv2.destroyAllWindows()
cam.release()
cv2.destroyAllWindows()


