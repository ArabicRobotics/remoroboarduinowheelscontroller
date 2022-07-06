
import imp
import threading
import time
import os
from clsRobot import Robot
from clsPSWorker import PSWorker
class PSMain (object):
	"""This class for """ 
	def __init__(self,robot):
		"""This initilization for 
		""" 
		try: 
			self.psWorker = PSWorker()
			self.psWorker.robot = robot
			self.threadPS = threading.Thread(target=self.psWorker.work)
			self.threadPS.start()
			return
		except Exception as e:
			print (e)
			return