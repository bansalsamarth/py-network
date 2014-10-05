from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 8001
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
	def handle(self):
		print '...connection established with:', self.client_address
		#Timestamp server - Prints out the time
		self.wfile.write('[%s] %s' %(ctime(), self.rfile.readline()))

tcpServ = TCP(ADDR, MyRequestHandler)
print 'Waiting for connection...'
tcpServ.serve_forever()