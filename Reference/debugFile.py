import cv2
import os
import math

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # This file should be the one that can detect faces. 

while(True):
    ret, img = cam.read()
    img = cv2.flip(img, -1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        radius = int(math.sqrt(((x + (w//2)) - x)**2 + ((y + (h//2)) - y)**2)) 
       # cv2.rectangle(img,(x,y),(x+w,y+h),(250,200,0),)
        cv2.circle(img, (x + (w//2), y + (h//2)), radius,(255,250,0), radius//8)
        
    cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
        
cam.release()
cv2.destroyAllWindows()

