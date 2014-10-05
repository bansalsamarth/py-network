#This is a timestamp TCP server that uses Twisted Internet classes.

from twisted.internet import protocol, reactor
from time import ctime

PORT = 8082

class TimeServProtocol(protocol.Protocol):
	
	#Executed when a client connects to us. Overriding the base class method
	def connectionMade(self):
		client = self.client = self.transport.getPeer().host
		print '...connected from : ', client
	
	#Called when a client sends a piece of data across the network
	#The reactor passes in the data as an argument to this method so that we can get access to it right
	#away without having to extract it ourselves.
	def dataReceived(self, data):
		self.transport.write('[%s] %s' %(ctime(), data))

#Create a protocol factory
#Called "factory" as an instance of our protocol is manufactured everytime
#we get an incoming connection

factory = protocol.Factory()
factory.protocol = TimeServProtocol
print 'Waiting for connection..'

#Installing a TCP listener to our reactor to check for service requests
#Whenever it receives a request, it creates TimeServProtocol instance
#to cater to the client
reactor.listenTCP(PORT, factory)
reactor.run()