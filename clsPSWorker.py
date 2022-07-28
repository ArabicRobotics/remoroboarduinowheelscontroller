from clsPS4Controller import PS4Controller, ControllerData
import threading
import time
import os
from clsRobot import Robot
from clsUtilities import MixedTools
class PSWorker (object):
	"""This class for """ 
	def __init__(self):
		"""This initilization for 
		""" 
		try: 
			self.controller = PS4Controller()             
			self.exit = False
			self.robot = None
			self.MegaSpeed=30
			self.mixedTools = MixedTools(self.MegaSpeed)         
			return
		except Exception as e:
			print (e)
			return
# threading Functions 
	def stop(self):
		""" This Method for  
		@type  paramName: Bool
		@param paramName : Description
		@rtype:  Boolean
		@return: True : everything went fine
		False : Something went wrong
		""" 
		try: 
			self.controller.stop()
			print ("controller stopped ")
			return True
		except Exception as e:
			print (e)
			return False
	def _start(self):
		try: 
			return self.controller.start()
		except Exception as e:
			print (e)
			return False
#endTHreading Functions 


	def work(self):
		""" This Method for  
		@type  paramName: Bool
		@param paramName : Description
		@rtype:  Boolean
		@return: True : everything went fine
		False : Something went wrong
		""" 
		try: 
			if self.controller.error == False:
				self._start()
				while True:
					if self.exit:
						return True

					if ControllerData.newData:
						#os.system('clear')
						#print (ControllerData.button_data)
						#print (ControllerData.axis_data)
						#print (ControllerData.R_Ball_H)
						#print (ControllerData.L_Ball_H)
						self.do()
						ControllerData.newData = False                
				return True
		except Exception as e:
			print (e)
			return False
	def do (self):
		""" This Method for  
		@type  paramName: Bool
		@param paramName : Description
		@rtype:  Boolean
		@return: True : everything went fine
		False : Something went wrong
		""" 
		try: 
			if ControllerData.L_Ball_H != None:
				if ControllerData.L_Ball_H !=0  or ControllerData.L_Ball_V !=0:
					self.move()
					#return True
			if ControllerData.R_Ball_H != None:
				print (ControllerData.R_Ball_H)
				if ControllerData.R_Ball_H!=0:
					self.rotate()
					#return True
			if self._checkOptions():
				if self.checkExit():
					self.controller.stop()
					self.exit= True
					return True
				if self.checkChangeRobot():
					return True
			return True
		except Exception as e:
			print (e)
			return False


	def checkChangeRobot(self):
			""" This Method for  
			@type  paramName: Bool
			@param paramName : Description
			@rtype:  Boolean
			@return: True : everything went fine
			False : Something went wrong
			""" 
			try:
				print ("Check Change Robot"+ str(ControllerData.Share))
				if ControllerData.Options== True:
					print ("changing Robot")
					self.robot.setActiveRobotOrNext()
					return True
				return False
			except Exception as e:
				print (e)
				return False 
	def _checkOptions(self):
			""" This Method for   Four Buttons
			@type  paramName: Bool
			@param paramName : Description
			@rtype:  Boolean
			@return: True : everything went fine
			False : Something went wrong
			""" 
			try: 
				
				if ControllerData.L1== True and  ControllerData.R1 ==True:
					print ("Options True")
					return True
				return False
			except Exception as e:
				print (e)
				return False
	def checkExit(self):
		""" This Method for   Options four bunntons +  + Share
		@type  paramName: Bool
		@param paramName : Description
		@rtype:  Boolean
		@return: True : everything went fine
		False : Something went wrong
		""" 
		try: 

			if ControllerData.button_data[8]== True:#shareButton#
				return True
			return False
		except Exception as e:
			print (e)
			return False 

	
	def move(self):
			""" This Method for  
			@type  paramName: Bool
			@param paramName : Description
			@rtype:  Boolean
			@return: True : everything went fine
			False : Something went wrong
			""" 
			try: 
				x = ControllerData.axis_data[0] 
				y = (ControllerData.axis_data[1]*-1) 
				angle =  ControllerData.getAngle360(0,0,x,y)
				print ("Moving Y : "+str(x)+ "  Y: "+ str(y)+" angle"+str(angle))
				moveData = self.mixedTools.convertAngleMove(angle,x*self.MegaSpeed,y*self.MegaSpeed)
                #moveData = MixedTools.convertAngleMove(str(angle),str(x*self.MegaSpeed),str(y*self.MegaSpeed))
				print (self.robot.move(moveData))
				#print self.robot.activeRobot.name
				#print self.robot.activeRobot.connection.defaultConnection
				#ledsRobot = self.robot.getByFunction(enumRobotAttributes.Leds)
				#ledsRobot.Leds.SetLed(enumLedName.progress,enumLedStatus.Dismiss)
				return True
			except Exception as e:
				print (e)
				return False

	def rotate(self):
			""" This Method for  
			@type  paramName: Bool
			@param paramName : Description
			@rtype:  Boolean
			@return: True : everything went fine
			False : Something went wrong
			""" 
			try: 				
				x = ControllerData.R_Ball_H *self.MegaSpeed
				print ("Rorating to "+str(x))
				values=[int(float(str(x)))      ,   -int(float(str(x)))     ,     int(float(str(x)))      ,  - int(float(str(x))) ]
				self.robot.move(values)
				return True
			except Exception as e:
				print (e)
				return False

if __name__ == "__main__":
	worker = PSWorker()
	worker.robot = Robot()
	worker.work()
	print ("robot will shutDown") 