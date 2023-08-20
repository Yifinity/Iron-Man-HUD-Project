class Recognizer:
    def __init__(self):
        # File to detect faces
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # This file should be the one that can detect faces. 
        pass

    def showFaces(self, img):
        # Convert img to grayscale
        print("Converting")
        processImg = cv2.flip(processImg, -1) # flip video image vertically
        gray = cv2.cvtColor(processImg, cv2.COLOR_BGR2GRAY)
        faces = self.face_detector.detectMultiScale(gray, 1.3, 5)

        # Present Detected Faces:
        for (x,y,w,h) in faces:
            print("Drawing")
            # Draw Rectangle at that location
            cv2.rectangle(img, (x,y), (x+w,y+h), HUDText, 2)
    

