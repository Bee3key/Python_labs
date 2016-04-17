import socketserver
import time

class MyTCPHandler(socketserver.BaseRequestHandler):

	def handle(self):
		self.data = time.ctime(time.time()) + "\r\n"
		print("{} wrote:".format(self.client_address[0]))
		print(self.data)
		self.request.sendall(self.data.encode('ascii'))

if __name__ == "__main__":
	HOST, PORT = "localhost", 8888

server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
server.serve_forever()