#!/usr/bin/python

import threading
import time

#globally shared buffers
exitapp = False
buffer0 = 20

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