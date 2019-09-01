LED_NUM = 31

servo1=30
servo2=31
servo1_pin=16
servo2_pin=18

from threading import Thread

import time
import json
import requests
import RPi.GPIO as GPIO

servo1=servo1-1
servo2=servo2-1


GPIO.setmode(GPIO.BOARD)

sense = 22
GPIO.setup(sense, GPIO.IN)

light=[3, 5, 7] #rgb
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

GPIO.setup(servo1_pin, GPIO.OUT)
GPIO.setup(servo2_pin, GPIO.OUT)

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
		for i in range(LED_NUM):
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

			r = GPIO.input(sense)
#			print r
			if r == 1:
				temp[i] = 0
			else:
				temp[i] = 1
				
			'''
			#print i, r
			if data[i] == 2:
				pass
			elif r == 1:
				data[i] = 0
			else:
				data[i] = 1
			'''
			time.sleep(0.0003)
			#print data
				

def post():
	while 1:
		dic={}
		for i in range(LED_NUM):
			dic[i+1] = temp[i]
		dic = json.dumps(dic)
		print dic
		s = requests.post('http://ericbottest1.azurewebsites.net/LED', data = dic)
		print s
		if s.status_code != 200:
			continue
		s = s.json()
#		print s
		for i in range(LED_NUM):
			st = str(i+1)
			data[i] = int(s[st])
		time.sleep(2)
		print data

def servo():
	s1_c = 10
	s2_c = 10
	p1=GPIO.PWM(servo1_pin,50)
	p2=GPIO.PWM(servo2_pin,50)
	p1.start(10)
	p2.start(10)
	while 1:
	#for i in range(5):

		if data[servo1] == 2:
			if s1_c != 15:
				p1.ChangeDutyCycle(5)
				s1_c = 15
				print '1'
		else:
			if s1_c != 10:
				p1.ChangeDutyCycle(10)
				s1_c = 10
				print '2'

		if data[servo2] == 2:
			p2.ChangeDutyCycle(5)
		else:
			p2.ChangeDutyCycle(10)
		time.sleep(1)
			

t1 = Thread(target = light_control)
t2 = Thread(target = post)
t3 = Thread(target = servo)

t1.start()
t2.start()
t3.start()
