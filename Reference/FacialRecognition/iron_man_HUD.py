import cv2
import os
import numpy as np
from PIL import Image
import math
import sqlite3
import time
from datetime import datetime
from iron_man_HUDTrain import getImagesAndLabels

#  As a convention, we will show the SQL keywords in uppercase and the parts of the command that we are adding (such as the table and column names) will be shown in lowercase.
conn = sqlite3.connect('names.sqlite')
cur = conn.cursor()

cur.execute('SELECT name FROM Names')
for row in cur:
    print(row[0])


# Path for face image database
path = 'dataset'
if not os.path.exists('dataset'):os.makedirs('dataset') # Create folder dataset. 
if not os.path.exists('trainer'):os.makedirs('trainer')

#names = ['None']
userName = ''

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

recognizer = cv2.face.LBPHFaceRecognizer_create()
#Write a try except statement here. 
recognizer.read('trainer/trainer.yml')
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # This file should be the one that can detect faces. 

def storeAndTrain():
    # Have Stream To Continue Here. 
    # cam.release()
    cv2.destroyAllWindows()
    userName = 'Unknown'
    notReady = True
    while notReady:
        userName = input("Enter the Name in the Database: ")
        notReady = not bool(input("Verify - Name: " + userName + " |[True:False]"))
    cur.execute('INSERT INTO Names (name) Values (?)', (userName,)) # Add new user into DB    
    conn.commit() # Now save it so it remebers it next time.
    cur.execute('SELECT name FROM Names') # Return a list of the selection
    face_id = len(cur.fetchall())-1 # Now take the length of the list - it will be the new index
    count = 0 # Now, take 30 photos
    print("Hold Still - make sure you're detected")
    cv2.imshow('HUD', img)
    while count < 30:
        ret, img = cam.read()
        img = cv2.flip(img, -1) # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        
        for (x,y,w,h) in faces:
            # Save the captured image into the datasets folder
            cv2.rectangle(img,(x,y),(x+w,y+h),HUDText,2)
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('HUD', img)
            count = count + 1 #increase count by one if we get a picture
            
    print("Image Collection Complete")
    print("Training")
   
    faces, ids = getImagesAndLabels(face_id) #This should work because there's only one person at a tie. 
    recognizer.train(faces, np.array(ids)) # You should train one at a time - face_id should work

    # Save the model into trainer/trainer.yml
    recognizer.write('trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi
    print("Training Complete")

#if Fix here 
#cur.execute("SELECT name FROM Names")
#if len(cur.fetchall()) < 2: # If it's only None
#   storeAndTrain() #Train it. 


while(True):
    now = datetime.now() # Current Date and Time.
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    # Built in camera read
    ret, img = cam.read()
    img = cv2.flip(img, -1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
#cv2.putText(img, text, (text_offset_x, text_offset_y), font, fontScale=font_scale, color=(0, 0, 0), thickness=1)
#    cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    for (x,y,w,h) in faces:
#        radius = int(math.sqrt(((x + (w//2)) - x)**2 + ((y + (h//2)) - y)**2)) 
 #       cv2.circle(img, (x + (w//2), y + (h//2)), radius, HUDText, radius//8)
        cv2.rectangle(img,(x,y),(x+w,y+h),HUDText,2)
        predictedId, confidence = recognizer.predict(gray[y:y+h,x:x+w]) # ID/Confidence
        if confidence <= 55:
            predictedId = 0
        cur.execute('SELECT name FROM Names') # Return list((x + (w//3)), (int(y + (h * 1.2))))
      
        cv2.putText(img,cur.fetchall()[predictedId][0], (x+5,y-5), font, 0.75, HUDText, 1)
        cv2.putText(img,str(math.floor(confidence)) + '%', (x + 5,y + h-5), font, 0.75, HUDText, 1)
        
        #cv2.putText(img,("User: " + cur.fetchall()[predictedId][0]), (10,85), font, 0.30, HUDText, 1)
        #cv2.putText(img,str(math.floor(confidence)) + '%', (x + 5,y + h-5), font, 0.30, HUDText, 1)
    #General Display
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
        #storeAndTrain()
        cv2.destroyAllWindows()
        
        
cur.close()
cam.release()
cv2.destroyAllWindows()
