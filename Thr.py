import time
import Queue

import threading 
customerq=Queue.Queue()
inputq=Queue.Queue()
outputq=Queue.Queue()


def stub_data():
	global customerq
	while(True):
		customerq.put("data")
		time.sleep(1)


def input_processor():
	global inputq
	while(True):
		inputq.put(customerq.get(True))

def worker1():
	while(True):
		global inputq,outputq
		data=inputq.get(True)
		data=data+"ONE"
		outputq.put(data)
def worker2():
	global inputq,outputq
	while(True):
		data=inputq.get(True)
		data=data+"TWO"
		outputq.put(data)
def printme():
	global outputq
	while(True):
		print outputq.get(True)


t=threading.Thread(target=stub_data)
t.start()
t=threading.Thread(target=input_processor)
t.start()
t=threading.Thread(target=worker1)
t.start()
t=threading.Thread(target=worker2)
t.start()
t=threading.Thread(target=printme)
t.start()
