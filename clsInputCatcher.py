import threading
from clsServerUtilities import ServerUtilities
from enums import *
from clsJsonFormatter import JsonFormatter
from clsUtilities import *
from clsRobot import Robot
from clsPSWorker import *
class InputCatcher(object):
	def __init__(self,socket):
		self.socket = socket
		self.robot = Robot()
		self.data = None
		self.psWorker = PSWorker()
		self.psWorker.robot = self.robot
		self.threadPS = threading.Thread(target=self.psWorker.work)
		self.threadPS.start()
		return

	def Catch(self,data=None):
		try:
			if len(data)>5:

				doThread = threading.Thread(target=self.do,args=(data,),name="ThreadingDoing")
				doThread.start()
			else:
				return False
		except Exception as e:
			print (e)
			return False

	def do(self,data):
		try:
			
			print(data)
			jsonData= JsonFormatter.getJsonfromString(data)
			print ("do--> json Data Json Formatter Getting .. Done")
			if jsonData != False:
				#self.socket.send(str(data))
				result = self.doAction(jsonData["com"],jsonData["params"],jsonData["requestId"])
			else:
				result = ServerUtilities.setResult("Json Error",False,enumEventType.Error,"")
				self.socket.send(str(result))
			return True
		except Exception as e:
			print (e)
			print ("error in Do ")
			try:
				doThread = threading.Thread(target=self.robot.move,args=(data,4,self.socket,0,),name="ThreadingDoing")
				doThread.start()
			except Exception as e:
				print ("error in move direct ")
				print (e)
				return False
			print ("Error in Do")
			print (e)
			return False

	def doAction(self,command,params,requestId=""):
		try:
			duration = 4
			result = ""
			print (" I am in doAction with "+str(params))
			while(switch(command)):
				if case("m"):
					print ("Command Is Move ")
					result = ServerUtilities.setResult("Movement Command Received",result,enumEventType.Success,requestId)
					self.socket.send(str(result))
					result = self.robot.move(params,duration,self.socket,requestId)
					if result:
						result = ServerUtilities.setResult("Movement Command Received",result,enumEventType.Success,requestId)
					else:
						result = ServerUtilities.setResult("Movement",result,enumEventType.Error,requestId)    						
					self.socket.send(str(result))
					return
				if (case("b")):
					result  = "Buzz"
					if result:
						result = ServerUtilities.setResult("Buzz",result,enumEventType.Success,requestId)
					else:
						result = ServerUtilities.setResult("Buzz",False,enumEventType.Error,requestId)    						
					self.socket.send(str(result))
					return
				return
			result = ServerUtilities.setResult("Not Existing Command ( Please send m ot b",False,enumEventType.Error,requestId)
			
			self.socket.send(str(result))

			return True
		except Exception as e:
			result = ServerUtilities.setResult("Error while doing the Action",e,enumEventType.Error,"")
			self.socket.send(str(result))
			print (e)
			return False
