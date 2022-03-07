from clsInputCatcher import  InputCatcher
import socket, threading
class ClientThread(threading.Thread):
	def __init__(self,clientAddress,clientsocket):
		threading.Thread.__init__(self)
		self.csocket = clientsocket
		self.clientAddress = clientAddress
		print ("New connection added: ", clientAddress)		
		self.catcher = InputCatcher(self.csocket)
	def run(self):
		try:
			print ("Connection from : ", self.clientAddress)
			#self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
			msg = ''
			while True:
				try:

					data = self.csocket.recv(2048)
					msg = data.decode()

					SocketSever.lastData = msg
					threadCatchData = threading.Thread(target=self.catcher.Catch,args=(msg,),name="ThreadCatchData")
					threadCatchData.start()

					if msg=='bye':
						break
				except Exception as e:
					print (e)
					print "Error in Data"
				print ("from client", SocketSever.lastData)
				self.csocket.send(bytes(msg,'UTF-8'))
			print ("Client at ", self.clientAddress , " disconnected...")
		except Exception as e:
			print "Error in Socket Server -- Run"
			print (e)
			return False
class SocketSever(object):
	lastData = None	
	def __init__(self):

		return
	def Start(self,HOST = "",PORT=12345):
		self.host = HOST
		self.port  = PORT
		self.server  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server.bind((self.host, self.port))
		print("Server started")
		print("Waiting for client request..")
		while True:
			self.server.listen(1)
			clientsock, clientAddress = self.server.accept()
			newthread = ClientThread(clientAddress, clientsock)
			newthread.start()

if __name__ == "__main__":
	server = SocketSever()
	server.Start()