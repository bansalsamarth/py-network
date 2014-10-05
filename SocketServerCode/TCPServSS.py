from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 8001
ADDR = (HOST, PORT)

#The StreamRequestHandler class treats input and output
#sockets as file-like objects


class MyRequestHandler(SRH):
	def handle(self):
		#Handle method in the base class (BaseRequest) is stubbed out
		print '...connection established with:', self.client_address
		#Timestamp server - Prints out the time
		self.wfile.write('[%s] %s' %(ctime(), self.rfile.readline()))

tcpServ = TCP(ADDR, MyRequestHandler)
print 'Waiting for connection...'
tcpServ.serve_forever()