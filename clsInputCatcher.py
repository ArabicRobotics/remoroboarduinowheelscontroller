import threading
from clsServerUtilities import ServerUtilities
from enums import *
from clsJsonFormatter import JsonFormatter
from clsUtilities import *
from clsRobot import Robot
class InputCatcher(object):
	def __init__(self,socket):
		self.socket = socket
		self.robot = Robot()
		return

	def Catch(self,data=None):
		try:
			doThread = threading.Thread(target=self.do,args=(data,),name="ThreadingDoing")
			doThread.start()
		except Exception as e:
			print (e)
			return False

	def do(self,data):
		try:
			
			print(data)
			jsonData= JsonFormatter.getJsonfromString(data)
			if jsonData != False:
				result = self.doAction(jsonData["com"],jsonData["params"],jsonData["requestId"])
			else:
				result = ServerUtilities.setResult("Json Error",False,enumEventType.Error,"")
				self.socket.send(bytes(str(result),'UTF-8'))
			return True
		except Exception as e:
			print (e)
			print "error in Do "
			return False

	def doAction(self,command,params,requestId="",duration=2):
		try:
			duration=eval(duration)
			print (" I am in doAction with "+str(params))
			while(switch(command)):
				if case("m"):
					result = self.robot.move(params,int(duration),self.socket,requestId)
					if result:
						result = ServerUtilities.setResult("Movement",result,enumEventType.Success,requestId)
					else:
						result = ServerUtilities.setResult("Movement",result,enumEventType.Error,requestId)    						
					self.socket.send(bytes(str(result),'UTF-8'))					
					return
				if (case("b")):
					result  = "Buzz"
					if result:
						result = ServerUtilities.setResult("Buzz",result,enumEventType.Success,requestId)
					else:
						result = ServerUtilities.setResult("Buzz",False,enumEventType.Error,requestId)    						
					self.socket.send(bytes(str(result),'UTF-8'))
					return
				return
			result = ServerUtilities.setResult("Not Existing Command ( Please send m ot b",False,enumEventType.Error,requestId)
			
			self.socket.send(bytes(str(result),'UTF-8'))

			return True
		except Exception as e:
			result = ServerUtilities.setResult("Error while doing the Action",e,enumEventType.Error,"")
			self.socket.send(bytes(str(result),'UTF-8'))
			print (e)
			return False
