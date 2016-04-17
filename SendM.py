import socket
import sys

HOST, PORT = "localhost", 9999
message = " ".join(sys.argv[1:])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	sock.connect((HOST, PORT))
	sock.sendall(bytes(message + "\n", "utf-8"))
	received = str(sock.recv(1024), "utf-8")
finally:
	sock.close()

print("Sent message: {}".format(message))
print("Received answer: {}".format(received))