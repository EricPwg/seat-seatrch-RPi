import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)

while(1):
	GPIO.output(3, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(3, GPIO.LOW)
	time.sleep(1)
