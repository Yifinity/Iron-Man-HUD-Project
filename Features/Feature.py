# Parent Class for global fonts
import cv2
from datetime import datetime
import math
import time


class Feature:
    def __init__(self):
        self.HUDText = (255,200,0)
        self.HUDColor = (207,172,50)
        self.font = cv2.FONT_HERSHEY_DUPLEX
        self.startTime = 0 
    
