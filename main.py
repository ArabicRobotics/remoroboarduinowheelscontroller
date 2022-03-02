from clsSocketServer import SocketSever
import sys
from clsInputCatcher import InputCatcher
def main():
	server = SocketSever()
	server.Start()

if __name__ == "__main__":
	main()

