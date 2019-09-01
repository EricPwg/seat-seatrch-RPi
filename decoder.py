import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(11, GPIO.IN)

def func(num):
	num = int(num)
	n1 = num % 2
	n2 = (num / 2) % 2
	n4 = (num / 4) % 2
	if n1 == 0:
		GPIO.output(3, GPIO.LOW)
	else:
		GPIO.output(3, GPIO.HIGH)

	if n2 == 0:
		GPIO.output(5, GPIO.LOW)
	else:
		GPIO.output(5, GPIO.HIGH)

	if n4 == 0:
		GPIO.output(7, GPIO.LOW)
	else:
		GPIO.output(7, GPIO.HIGH)
	

def wri(d, fp):
	f = open(fp, 'w')
	for i in range(len(d)):
		f.write(str(d[i]))
		f.write('\n')
	f.close()

d = []

bff = open('button_data.txt', 'r')
bf = bff.readlines()
for i in range(len(bf)):
	t = bf[i].split()[0]
	d.append(int(t))
bff.close()

while(1):
	'''
	x = raw_input('Please input the number(0~7), q to quit:')
	try:
		int(x)
		func(x)
	except:
		if x == 'q' or x == 'Q':
			break
		else:
			print 'please input A number ONLY.'
	a = GPIO.input(11)
	print a
	'''

	f=open('data', 'r')
	f=f.readlines()
#	print f
	stage=[]
	for i in range(len(f)):
		tt = f[i].split()[0]
		stage.append(int(tt))
	print 'stage'
	print stage
	for i in range(32):
		GPIO.output(13, GPIO.LOW)
		func(i)
		if i<8 and stage[i] == 1:
			GPIO.output(13, GPIO.HIGH)
		else:
			GPIO.output(13, GPIO.LOW)
		
		if (i > 7):
			GPIO.output(15, GPIO.LOW)
		else:
			GPIO.output(15, GPIO.HIGH)
		
		ii = GPIO.input(11)
		print d
		if i<8 and d[i] != ii:
			d[i] = ii
			wri(d, 'button_data.txt')
#		print i
		print d
		time.sleep(0.0003)
