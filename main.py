# import os
import numpy
import cv2
# from PIL import Image

# Set Dimensions
screenWidth = 800
screenHeight = 480 

# Define / Setup Camera 
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 30)

def main():
    while True:
        ret, image = cam.read()
        image = cv2.resize(image, (screenWidth, screenHeight), fx = 0, fy =  0, interpolation = cv2.INTER_CUBIC)
        height, width = image.shape[:2]
        print("Height:", height, "by Width:", width)
        cv2.imshow('IMAGETEST', image)
        k = cv2.waitKey(1)
        if k != -1:
            break

    cam.release()
    cv2.destroyAllWindows()


main()
