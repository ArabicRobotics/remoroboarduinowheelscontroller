
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
			self.ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=.7)
			self.result=None
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
					print ("port is opened!")
					self.ser.close()
				if open:
					self.ser.open()
				else:
					print ("port is Closed!")
				return true
			except IOError: # if port is already opened, close it and open it again and print message
				ser.close()
				ser.open()
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
		except Exception as e:
			print (e)
			return False

	def close(self,open=False):
		"""This initilization for 
		""" 
		try:
			if self.ser.isOpen():
				print ("port is opened!")
				self.ser.close()
				return True
			return True
			self.checkConnection(True)
		except Exception as e:
			print (e)
			return False

if __name__ == "__main__":
	connection = Connection()
	connection.checkConnection()