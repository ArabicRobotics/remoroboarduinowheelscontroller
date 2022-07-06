
import imp
import threading
import serial
import time
from clsServerUtilities import ServerUtilities
from enums import *
from clsJsonFormatter import JsonFormatter
class Connection (object):
	"""This class for """ 
	def __init__(self):
		"""This initilization for 
		""" 
		try:
			self.ser =  serial(port='/dev/ttyUSB0', baudrate=9600, timeout=.7)
			self.result=None
			self.lastRead = None
			self.isReading=False
			self.threadReading=None
			return
		except Exception as e:
			print (e)
			return

	def checkConnection(self,open=False):
		"""This initilization for 
		""" 
		try:
			try:
				if self.ser.isOpen():
					print ("Port is Opened!")
					self.ser.close()
				if open:
					self.ser.open()
				else:
					print ("Port is Closed!")
				return True
			except IOError: # if port is already opened, close it and open it again and print message
				self.ser.close()
				self.ser.open()
				print ("port was already open, was closed and opened again!")
				return False
		except Exception as e:
			print (e)
			return False

	def open(self,open=False):
		"""This initilization for 
		""" 
		try:
			self.checkConnection(True)
			if (self.isReading==False):
				self.threadReading = threading.Thread(target=self.reader,name="Thread Reading ..")
				self.threadReading.start()
		except Exception as e:
			print (e)
			return False

	def close(self,open=False):
		"""This initilization for 
		""" 
		try:
			if self.ser.isOpen():
				print ("port is open!")
				self.ser.close()
				print ("port is now Closed!")
				return True
			return True
			self.checkConnection(True)
		except Exception as e:
			print (e)
			return False

	def send(self,x):
		try:
			writeFeedback = self.ser.write(str.encode((x)))
			print ("Message Sent "+str(x))
			return writeFeedback
		except Exception as e:
			print ("Error in Send ")
			print (e)
			return False

	def read(self):
		try:
			data = self.ser.readline()
			return data
		except Exception as e:
			print (e)
			return False

	def reader(self):
		try:
			while (True):
				time.sleep(0.3)
				if self.ser.in_waiting:
					self.lastRead = self.read()
					print (self.lastRead)
		except Exception as e:
			print (e)
			return False


if __name__ == "__main__":
	connection = Connection()
	connection.checkConnection(True)
	print ("sleeping 5 after open Connection ")
	time.sleep(5)
	print (connection.send ("A"))
	print ("message Sent")
	time.sleep(1)
	print ("read feedback")
	print (connection.read())
	print ("wait for while to enjoy the wheels ..... ")
	time.sleep(10)
	print ("Stop the car ")
	connection.send("z")
	print ("Done All will exit")
	
	connection.close()

