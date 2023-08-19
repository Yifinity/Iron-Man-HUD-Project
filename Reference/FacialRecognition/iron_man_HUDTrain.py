#This should be the for store and train.
import cv2
import numpy as np
from PIL import Image
import os

path = 'dataset'
recognizer = cv2.face.LBPHFaceRecognizer_create() # Should create the recognizer
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

def getImagesAndLabels(userId):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []
    for imagePath in imagePaths: # For each image file - 
        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8') # OHH So this should be a table of sorts - with the images, and the box corrdiates for each one. 

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = face_detector.detectMultiScale(img_numpy) # Go through images

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w]) # For the x, y, w, h corrordinate in each face, add the box the face
            ids.append(id)
    return faceSamples, ids
