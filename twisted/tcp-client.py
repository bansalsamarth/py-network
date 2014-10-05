#This is a timestamp TCP client

from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 8082

class TimeClientProtocol(protocol.Protocol):
	def sendData(self):
		data = raw_input('>')
		if data:
			print '...sending %s ...' %data
			self.transport.write(data)
		else:
			self.transport.loseConnection()

	def connectionMade(self):
		self.sendData()

	def dataReceived(self, data):
		print data
		self.sendData()

#Creating a client factory.

class TimeClientFactory(protocol.ClientFactory):
	protocol = TimeClientProtocol
	clientConnectionLost = clientConnectionFalied = \
		lambda self, connector, reason: reactor.stop()

#Make aconnection to the server and run the reactor. 
reactor.connectTCP(HOST, PORT, TimeClientFactory())
reactor.run()