from clsWheels import Wheels
import threading
import time
from clsServerUtilities import ServerUtilities
from enums import *
from clsJsonFormatter import JsonFormatter
class Robot (object):
	"""This class for """ 
	def __init__(self):
		"""This initilization for 
		""" 
		try: 
			self.wheels =Wheels()
			return
		except Exception as e:
			print (e)
			return
	def move(self,values,duration,socket=None,requestId=None):
		""" This Method for  
		@type  paramName: Bool
		@param paramName : Description
		@rtype:  Boolean
		@return: True : everything went fine
		False : Something went wrong
		""" 
		try: 
			print " I am in Robot-move"
			result = self.wheels.move(values,duration)
			if result == True:
				result = ServerUtilities.setResult("Robot Movement",result,enumEventType.Success,requestId)
				socket.send(str(result))
				return True
			else:
				result = ServerUtilities.setResult("Robot Movement",result,enumEventType.Error,requestId)
				socket.send(str(result))
				return False
		except Exception as e:
			result = ServerUtilities.setResult("Robot Movement",e,enumEventType.Error,requestId)
			socket.send(str(result))			
			print(e)
			return False

	"""
	def _buzz(self,OnOff,duration):

		try: 
			print ("buzzing ")
			result = self.robot.Buzzer_control(OnOff)  #buzzer off"
			if duration>0:
				time.sleep(duration)
				result = self.robot.Buzzer_control(0)  #buzzer off"
			return True
		except Exception as e:
			print(e)
			return False



	def buzz(self,OnOff =0,duration=1,socket=None,requestId=None):
		 This Method for  
		try: 
			threading.Thread(target=self._buzz,args=(OnOff,duration,),name="ThreadMove").start()
			result = ServerUtilities.setResult("Robot Buzz",True,enumEventType.Success,requestId)
			self.socket.send(str(result))
			return True
		except Exception as e:
			result = ServerUtilities.setResult("Robot Buzz",e,enumEventType.Error,requestId)
			self.socket.send(str(result))
			print(e)
			return False
	"""

#robot = Robot()
#robot.move("10,10,10,10",1,)
#robot.buzz(1,1)
