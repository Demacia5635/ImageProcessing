#!/usr/bin/env python

import socket
import sys
import coordinates

class Network:
	def __init__(self, ip):
		self.port = 42069
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_address = (ip, self.port)
		#self.ip = ip
		print("Attempting to connect to "+str(ip)+":"+str(self.port))
		self.sock.connect(self.server_address)

	def send(self, coordinates):
		try:
			message = str(coordinates)
			print("Sent " + message)
			#self.sock.sendall(message)
			self.sock.sendto(message.encode('utf-8'), self.server_address[0])

			amount_received = 0
			amount_expected = len(message)

			while amount_received < amount_expected:
				data = self.sock.recv(16)
				amount_received += len(data)
		except:
			print("FUCK YOU")
