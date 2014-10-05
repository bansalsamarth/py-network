#http://www.acmesystems.it/python_httpserver

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os

PORT_NUMBER = 8080

def set_mime_type(url):
	a = {
		'.html'	:	'text/html',
		'.jpg'	:	'image/jpg',
		'.gif'	:	'image/gif',
		'.js'	:	'application/javascript',
		'.css'	:	'text/css',
	}
	for extension, mime_type in a.iteritems():
		if url.path.endswith(extension):
			return mime_type
	return False

#Handle any incoming request from browser
class MyHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		if self.path == '/':
			self.path = "index.html"

		try:
			#Set the MIME type based on file type
			mime = set_mime_type(self)
			if mime:
				#Open the static file and serve
				f = open(os.curdir + os.sep + self.path)
				self.send_response(200)
				self.send_header('Content-Type', mime)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			else:
				self.send_error(404, 'aaFile not found : %s' %self.path)

			return

		except IOError:
			self.send_error(404, 'aaFile not found : %s' %self.path)

try:
	server = HTTPServer(('', PORT_NUMBER), MyHandler)
	print "Started web server on port ", PORT_NUMBER
	server.serve_forever()

except KeyBoardInterrupt:
	print "Shutting down the server"
	server.socket.close()