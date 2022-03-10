from clsSocketServer import SocketSever
import sys
from clsInputCatcher import InputCatcher
def main():
	server = SocketSever()
	server.Start()

# Message Example     {"com": "m","params": [1,-200,3,4], "requestId": "2"}  
if __name__ == "__main__":
	main()

