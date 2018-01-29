#!/usr/bin/env python

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 42069)
print("Hi!")
#print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

sock.listen(1)

while True:
	#k = cv2.waitKey(1) & 0xFF
	#if k == ord('q'):
	#	break
	#print >>sys.stderr, 'waiting for a connection'
	connection, client_address = sock.accept()

	try:
		# Receive the data in small chunks and retransmit it
		while True:
			print("Connected")
			data, serverAddress = connection.recvfrom(message.decode('utf-8'))
			#data = connection.recv(16)
			print >>sys.stderr, 'Received "%s"' % data
		'''
			if data:
				#print >>sys.stderr, 'sending data back to the client'
				connection.sendall(data)
			else:
				#print >>sys.stderr, 'no more data from', client_address
				break
		'''

	finally:
		# Clean up the connection
		connection.close()
print("Bye!")
