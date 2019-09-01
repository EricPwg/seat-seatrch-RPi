import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

light_pin=[3, 5, 7]
GPIO.setup(light_pin[0], GPIO.OUT)
GPIO.setup(light_pin[1], GPIO.OUT)
GPIO.setup(light_pin[2], GPIO.OUT)

select=[8, 10, 12, 11, 13, 15]
GPIO.setup(select[0], GPIO.OUT)
GPIO.setup(select[1], GPIO.OUT)
GPIO.setup(select[2], GPIO.OUT)
GPIO.setup(select[3], GPIO.OUT)
GPIO.setup(select[4], GPIO.OUT)
GPIO.setup(select[5], GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

def func(num):
	num = int(num)
	n32 = (num/32) % 2
	n16 = (num/16) % 2
	n8 = (num/8) % 2
	n4 = (num/4) % 2
	n2 = (num/2) % 2
	n1 = (num) % 2

	if n1 == 0:
		GPIO.output(select[0], GPIO.LOW)
	else:
		GPIO.output(select[0], GPIO.HIGH)

	if n2 == 0:
		GPIO.output(select[1], GPIO.LOW)
	else:
		GPIO.output(select[1], GPIO.HIGH)

	if n4 == 0:
		GPIO.output(select[2], GPIO.LOW)
	else:
		GPIO.output(select[2], GPIO.HIGH)

	if n8 == 0:
		GPIO.output(select[3], GPIO.LOW)
	else:
		GPIO.output(select[3], GPIO.HIGH)

	if n16 == 0:
		GPIO.output(select[4], GPIO.LOW)
	else:
		GPIO.output(select[4], GPIO.HIGH)

	if n32 == 0:
		GPIO.output(select[5], GPIO.LOW)
	else:
		GPIO.output(select[5], GPIO.HIGH)

while 1:
	r = raw_input()
	func(r)
	for i in range(50):
		GPIO.output(16, GPIO.HIGH)
		time.sleep(0.0001)
		GPIO.output(16, GPIO.LOW)
		time.sleep(0.0009)
	print r
