import threading
from clsUtilities import MixedTools
import time
#from Raspblock import Raspblock
class Wheels (object):
	def __init__(self,connection):
		"""This initilization for 
		""" 
		try: 
			#self.robot = robot
			self.mixedTools = MixedTools()
			self.connection = connection
			self.connection.open()
			return
		except Exception as e:
			print(e)
			return
	def _move(self,values,duration):
		""" This Method for
		@type  paramName: Bool
		@param paramName : Description
		@rtype:  Boolean
		@return: True : everything went fine
		False : Something went wrong
		""" 
		try: 
			result = ""
			print ("I am in _move ")
			print (values)
			print (duration)
			print ("End Print Move")
			message = "<"+self.mixedTools.ArrayToString(values)+","+str(duration)+">"
			self.connection.send(message)
			#result = self.robot.Speed_Wheel_control(values[0],values[1], values[2],values[3])      #All wheel forward with 2 speed"
			if duration>0:
				time.sleep(duration)
				#self.robot.Speed_Wheel_control(0,0,0,0) 
			return result
		except Exception as e:
			print ("Error in wheels._move")
			print(e)
			return False
	def move(self,values,duration=10):
		""" This Method for
		@type  paramName: Bool
		@param paramName : Description
		@rtype:  Boolean
		@return: True : everything went fine
		False : Something went wrong
		""" 
		try: 
			print ("I am in wheels-move")
			print (values)

			#robot.Speed_Wheel_control(2, 2, 2, 2)      #All wheel forward with 2 speed"
			#self._move(values,duration)

			threadMoving = threading.Thread(target=self._move,args=(values,duration,),name="threadMoving")
			threadMoving.start()
			return True
		except Exception as e:
			print(e)
			return False