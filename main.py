from concurrent.futures import thread
import imp
import threading
from clsSocketServer import SocketSever
import sys
from clsInputCatcher import InputCatcher
from clsRobot import Robot
from clsPSMain import PSMain
def main():
	robot = Robot()
	server = SocketSever(robot)
	t= threading.Thread(target =server.Start)
	ps= PSMain(robot)
	t.start()
# Message Example     {"com": "m","params": [1,-200,3,4], "requestId": "2"}  
if __name__ == "__main__":
	main()

