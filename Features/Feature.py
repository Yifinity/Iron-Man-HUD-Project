# Parent Class for global fonts
import cv2

class Feature:
    def __init__(self):
        self.HUDText = (255,200,0)
        self.HUDColor = (207,172,50)
        self.font = cv2.FONT_HERSHEY_DUPLEX
        self.startTime = 0 
    
