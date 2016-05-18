from socket import *
import time

sock = socket(AF_INET, SOCK_STREAM) # make socket TCP
sock.bind(('', 8888))					# bind socket to port 8888
sock.listen(5) 						# goes to listen mode for 5 connections

print (sock.accept())
client, addr = sock.accept() 	#accept connection 
print ("connection from address %s " % str(addr))
timestr = time.ctime(time.time()) + "\r\n"
client.send(timestr.encode('ascii'))
client.close()
