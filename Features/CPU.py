# Get CPU Info
from Features.Feature import *

class Clock(Feature):
    def __init__(self):
        # Inherit nessisary fonts
        super().__init__()
        # Put on right side
        self.tempPos = (700, 50)

    def onStep(self):
        # Give us our temperature
        self.cpuTemp = CPUTemperature()

    def redraw(self, img):
        cv2.putText(img, self.cpuTemp, self.tempPos, self.font, 0.5,
                     self.HUDText, 1)
         