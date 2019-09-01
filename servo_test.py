import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.OUT)

p1 = GPIO.PWM(16, 50)
p1.start(10)
time.sleep(1)
