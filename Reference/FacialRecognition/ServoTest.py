from gpiozero import Servo
from time import sleep

servo = Servo(2,initial_value=0, min_pulse_width=1/1000, max_pulse_width=2/1000)

#print(servo.max_pulse_width())


try:
    while True:
        servo.min()
        sleep(2)
        servo.mid()
        sleep(2)
        servo.max()
        sleep(2)
except KeyboardInterrupt:
    print("Program stopped")