# Feature for FPS and Time

from datetime import datetime
import math
import time
import Feature


class Clock(Feature):
    def __init__(self):
        # Inherit nessisary fonts
        super().__init__(self)
        self.timePos = (10, 75)
        self.fpsPos = (10, self.timePos[1] + 20)

    def onStep(self):
        self.now = datetime.now() # Current Date and Time.
        # Format time 
        self.date_time = self.now.strftime("%B %d, %Y | %I:%M%p")

        # FPS Calculation
        self.timeNow = time.time()
        self.fps = 1 / (self.timeNow - self.startTime)
        self.startTime = self.timeNow
    
    def redraw(self, img):
        cv2.putText(img, self.date_time, self.timePos, self.font, 0.5,
                     self.HUDText, 1)
        
        cv2.putText(img, ("FPS: "+ str(math.floor(self.fps))), self.fpsPos,
                     self.font, 0.5, self.HUDText, 1)      
        