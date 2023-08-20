# Get CPU Info
from Features.Feature import *

class CPU(Feature):
    def __init__(self):
        # Inherit nessisary fonts
        super().__init__()
        # Put on right side
        self.tempPos = (500, 50)

    def onStep(self):
        # Give us our temperature
        self.cpuTemp = int(CPUTemperature().temperature)
    def redraw(self, img):
        cv2.putText(img, f'Temperature: {self.cpuTemp} C', self.tempPos, self.font, 0.5,
                     self.HUDText, 1)
         