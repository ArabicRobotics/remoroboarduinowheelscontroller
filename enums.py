
from enum import Enum
from clsUtilities import *

#To Add more to enum
# 1- add to EnumItem
# 2- Add if statement to the switch
#Thats it :)
def case(*args):
	return any((arg == switch.value for arg in args))


#region Events





class enumExcecutionMood(Enum):
	Debug= enumItem("Debug",0,"")
	Test =enumItem("Test",1,"")
	Live = enumItem("Live",2,"")
	@staticmethod
	def ByVal(value): 
		while(switch(value)):
			if case(0):
				return enumExcecutionMood.Debug

			if (case(1)):
				return enumExcecutionMood.Test
			if (case(2)):
				return enumExcecutionMood.Live

class enumEventNotificationWay(Enum):
	Print= enumItem("PrintEvent",0,"Print Event on Screen")
	Led= enumItem("Led Notification",1,"")

class enumEventCategory(Enum):
	System = enumItem("System",0,"")
	User = enumItem("User",1,"")
	Hardware= enumItem("Hardware",2,"")

class enumEventLevel(Enum):
	NeedAttention= enumItem("NeedAttention",0,"")
	CoreError =enumItem("CoreError",1,"")
	Normal = enumItem("Normal",2,"")
	
class enumNotificationSource(Enum):
	ServerRobot = enumItem("Server Robot","1","")
	Application = enumItem("Robot Application","2","")
	Movement = enumItem("Robot Movement","3","")
	Leds = enumItem("Robot LEDS","5","")
	Camera = enumItem("Robot Camera","6","")
	Connection = enumItem("Robot Connection","7","")
	Chat = enumItem("Robot Chat","8","")
	WebForm = enumItem("Web Form","11","")
	WebServer = enumItem("Web Server","12","")

class enumNotificationLevel(Enum):
	Error = enumItem("Error","1","")
	Worning = enumItem("Worning","2","")
	Notification = enumItem("Notification","3","")

class enumEventType(Enum):
	Information  = enumItem("Information",0," ")
	Worning =enumItem("Warning",1," ")
	Error = enumItem("Error",2," ")
	Cretical =enumItem("Critical",3," ")
	Success=enumItem("Success",4," ")

class enumEventStatus(Enum):
	Read = enumItem("Read",0," ")
	Handled = enumItem("Handled",1," ")
	Unread = enumItem("Unread",2," ")
	OneTimeShow = enumItem("OneTimeShow",3,"")


class enumDirection(Enum):
	Left = enumItem("Left",0," ")
	Right = enumItem("Right",1," ")
	Up = enumItem("Up",2," ")
	Down = enumItem("Down",3,"")
	Stop = enumItem("Stop",4,"")



class enumEventSource(Enum):
	Server  = enumItem("Server",0," ")
	Connection=enumItem("Connection",1," ")
	Core = enumItem("Core",2," ")
	Robot = enumItem("Robot",3," ")



class enumEventDistenation(Enum):
	Log = enumItem("Log",0,"")
	Database = enumItem("Log",1,"")
#endregion



class enumComunicationType(Enum):
	"""Robot RobotFunction )
	"""
	set = enumItem("set","0","")
	get = enumItem("get","1","")






class enumComunicationDataType(Enum):
	"""Robot RobotFunction )
	"""
	raw = enumItem("raw","0","")
	parameters = enumItem("parameters","1","")
	hexa = enumItem("Hexa","2","")
	@staticmethod
	def ByVal(value):
		"""Get the enum by value

		@type  value:int
		@param value:
		Received=0 , ... for more in the server Request Status
		"""
		while switch(value):
			if case(0):
				return enumComunicationDataType.raw
			if case(1):
				return enumComunicationDataType.parameters
			if case(2):
				return enumComunicationDataType.hexa
			return


########## robot Types ###########
class enumRobotAttributes(Enum):
	"""Robot RobotFunction )
	"""
	Motion = enumItem("function",0,"Motion")
	Leds = enumItem("function",1,"Leds")
	Lights = enumItem("function",2,"Lights")
	Moving =  enumItem("function",3,"Moving")
	Sensors =  enumItem("function",4,"Sensors")
	Camera =  enumItem("function",5,"Camera")
	Chat =  enumItem("function",6,"Chat")
	Screen = enumItem("function",7,"Screen")
	
	Count=enumItem("count",8,"FunctionsCount")
	
	@staticmethod
	def ByVal(value):
		"""Get the enum by value

		@type  value:int
		@param value:
		Received=0 , ... for more in the server Request Status
		"""
		while switch(value):
			if case(0):
				return enumRobotAttributes.Motion

			if case(1):
				return enumRobotAttributes.Leds

			if case(2):
				return enumRobotAttributes.Lights

			if case(3):
				return enumRobotAttributes.Moving

			if case(4):
				return enumRobotAttributes.Sensors

			if case(5):
				return enumRobotAttributes.Camera
			if case(6):
				return enumRobotAttributes.Chat
			if case(7):
				return enumRobotAttributes.Screen
			return False











class enumDataType():
			Picture=0
			Voice=1
			Text= 2

def main():
	leds = enumRobotAttributes.Leds
	print (enumComunicationDataType.parameters.value.value)
	print(len(enumRobotAttributes))
	print(enumRobotAttributes.Chat.value.description)
	print(enumRobotAttributes.Chat.value.name)

if __name__ == '__main__':
	main()