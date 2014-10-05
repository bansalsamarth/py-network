#http://www.acmesystems.it/python_httpserver

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

#BaseHTTPRequestHandler - Docs
#This class is used to handle the HTTP requests that arrive at the server. 
#By itself, it cannot respond to any actual HTTP requests; it must be subclassed to 
#handle each request method (e.g. GET or POST). 
#BaseHTTPRequestHandler provides a number of class and instance variables, and methods for use by subclasses.

#The handler will parse the request and the headers, then call a method specific to the request type. 
#The method name is constructed from the request. 
#For example, for the request method SPAM, the do_SPAM() method will be called with no arguments. 
#All of the relevant information is stored in instance variables of the handler. 
#Subclasses should not need to override or extend the __init__() method.

#HTTPServer - Docs
#This class builds on the TCPServer class by storing the server address as instance variables named
#server_name and server_port. The server is accessible by the handler, 
#typically through the handler's server instance variable

PORT_NUMBER = 8080

class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-Type', 'text/html')
		self.end_headers()

		#wfile - Contains the output stream for writing a response back to the client. 
		#Proper adherence to the HTTP protocol must be used when writing to this stream.
		self.wfile.write("Hello World!")

try:
	server = HTTPServer(('', PORT_NUMBER), MyHandler)
	print "Started HTTP Server on Port ", PORT_NUMBER
	server.serve_forever()

except KeyboardInterrupt:
	print "Shutting down the web server"
	server.socket.close()