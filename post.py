LED_DATA_FILE = 'data'

import requests
import time
import json

def pos(d):
	dic={}
	for i in range(len(d)):
		dic[i] = d[i]
	dic = json.dumps(dic)
	print dic
	s = requests.post('http://ericbottest1.azurewebsites.net/LED', data = dic)
	print s
	s = s.json()
	print s
	
	f = open(LED_DATA_FILE, 'w')
	for i in range(len(s)):
		inf = str(i)
		f.write(str(s[inf])+'\n')
	f.close()

f = open('button_data.txt', 'r')
f = f.readlines()

d = []
for i in range(len(f)):
	t = f[i].split()[0]
	d.append(int(t))

print 'start'
pos(d)
print 'ok'
while 1:
	time.sleep(1)
	print d
	f = open('button_data.txt', 'r')
	f = f.readlines()
	flag = 0
	for i in range(len(f)):
		t = int(f[i].split()[0])
		if d[i] != t:
			d[i] = t
			flag = 1
	if flag == 1:
		pos(d)
	else :
		pass
