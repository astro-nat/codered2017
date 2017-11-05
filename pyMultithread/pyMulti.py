#!/usr/bin/python

import threading
import time
#import serial

#globally shared buffers
buffer0 = 0
buffer1 = []
buffer2 = []
buffer3 = []
buffer4 = []

#global exit variable
exitapp = False

class RecordThread(threading.Thread):
	#initialization function
	def __init__(self, threadID, name):
		#initialize threading stuff
		threading.Thread.__init__(self)

		#set input arguements as variables of the object
		self.threadID = threadID
		self.name = name

	#run this function while executing the thread
	def run(self):
		global buffer0, exitapp
		print "Starting " + self.name

		while not exitapp:
			print buffer0
			buffer0 += 20
			time.sleep(5)

		print "Exiting " + self.name

	#add arduino serial data to buffer
	def recordToBuffer(self):
		global buffer0, buffer1, buffer2, buffer3, buffer4
		return

	#if buffer reaches past predefined size, concatenate from begining (FIFO)
	def maintainBufferSize(self):
		global buffer0, buffer1, buffer2, buffer3, buffer4
		bufferSize = 1000
		return

class ParseThread(threading.Thread):
	#initialization function
	def __init__(self, threadID, name):
		#initialize threading stuff
		threading.Thread.__init__(self)

		#set input arguements as variables of the object
		self.threadID = threadID
		self.name = name

	#run this function while executing the thread
	def run(self):
		global buffer0, exitapp
		print "Starting " + self.name

		while not exitapp:
			print buffer0
			time.sleep(1)

		print "Exiting " + self.name

	#if buffer reaches past predefined size, concatenate from begining (FIFO)
	def maintainBufferSize(self):
		global buffer0, buffer1, buffer2, buffer3, buffer4
		bufferSize = 1000
		return

#create new thread objects (dont run yet)
thread1 = RecordThread(1, "arduino_recording_thread")
thread2 = ParseThread(2, "parse_buffer_thread")

try:
	#run the run function in the threads
	thread1.setDaemon(True)  # very important
	thread2.setDaemon(True)  # very important
	thread1.start()
	thread2.start()

	#shoddy break
	while True:
		pass
except (KeyboardInterrupt, SystemExit):
	exitapp = True
	raise

print "Exiting Main Thread"