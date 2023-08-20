import cv2

class Recognizer:
    def __init__(self):
        # File to detect faces
        self.face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # This file should be the one that can detect faces. 
       
    def showFaces(self, img):
        # Convert img to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_detector.detectMultiScale(gray, 1.3, 5)
        cv2.putText(img, f'Faces Found: {len(faces)}', (10,135),  cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 200, 0), 2)
        # Present Detected Faces:
        print(faces)
        for (x,y,w,h) in faces:
            # Draw Rectangle at that location

            cv2.rectangle(img, (x,y), (x+w,y+h), (255, 200, 0), 2)
    

