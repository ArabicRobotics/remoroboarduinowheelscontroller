from threading import Thread
import time
#from Raspblock import Raspblock
class Wheels (object):
	def __init__(self,robot):
		"""This initilization for 
		""" 
		try: 
			self.robot = robot
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
			#result = self.robot.Speed_Wheel_control(values[0],values[1], values[2],values[3])      #All wheel forward with 2 speed"
			if duration>0:
				time.sleep(duration)
				#self.robot.Speed_Wheel_control(0,0,0,0) 
			return result
		except Exception as e:
			print(e)
			return False
	def move(self,values,duration):
		""" This Method for
		@type  paramName: Bool
		@param paramName : Description
		@rtype:  Boolean
		@return: True : everything went fine
		False : Something went wrong
		""" 
		try: 
			print (values)
			self.decodeValues(values,duration)
			#robot.Speed_Wheel_control(2, 2, 2, 2)      #All wheel forward with 2 speed"
			return True
		except Exception as e:
			print(e)
			return False
	def decodeValues(self,values,duration=10):
		try:
			intValues =  list(str(values).split(','))
			finalValues=[]
			for val in intValues:
				finalValues.append(int(val))
			print (finalValues)
			Thread(target=self._move,args=(finalValues,duration,),name="ThreadMove").start()
			
			#self._move(intValues,duration)
			return True
		except Exception as e:
			print(e)
			return False
