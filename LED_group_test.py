from threading import Thread

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

light=[3, 5, 7]
GPIO.setup(light[0], GPIO.OUT)
GPIO.setup(light[1], GPIO.OUT)
GPIO.setup(light[2], GPIO.OUT)

select=[8, 10, 12, 11, 13, 15]
GPIO.setup(select[0], GPIO.OUT)
GPIO.setup(select[1], GPIO.OUT)
GPIO.setup(select[2], GPIO.OUT)
GPIO.setup(select[3], GPIO.OUT)
GPIO.setup(select[4], GPIO.OUT)
GPIO.setup(select[5], GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

data=[0 for i in range(LED_NUM)]

temp=[0 for i in range(LED_NUM)]

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
'''
while 1:
	r = raw_input()
	func(r)
	for i in range(50):
		GPIO.output(16, GPIO.HIGH)
		time.sleep(0.0001)
		GPIO.output(16, GPIO.LOW)
		time.sleep(0.0009)
	print r
'''
def color(r, g, b):
	if r == 0:
		GPIO.output(light[0], GPIO.LOW)
	else:
		GPIO.output(light[0], GPIO.HIGH)

	if g == 0:
		GPIO.output(light[1], GPIO.LOW)
	else:
		GPIO.output(light[1], GPIO.HIGH)

	if b == 0:
		GPIO.output(light[2], GPIO.LOW)
	else:
		GPIO.output(light[2], GPIO.HIGH)
	
	

def light_control():
	while 1:
		for i in range(32):
			color(0,0,0)
			func(i)
			
			if data[i] == 0:
				color(0,1,0)
			elif data[i] == 1:
				color(1,0,0)
			elif data[i] == 2:
				color(0,0,1)
			else:
				color(0,0,0)
			time.sleep(0.0003)
#			print data
				

def tt():
	while 1:
		r = raw_input()
		r = r.split()
		data[int(r[0])] = int(r[1])

t1 = Thread(target = light_control)
t2 = Thread(target = tt)

t1.start()
t2.start()
