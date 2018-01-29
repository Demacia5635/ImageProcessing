#!/usr/bin/env python

import sys
import cv2
import camera
import worker
import time
import coordinates
import network2 as network

#to be removed after deployment
class PictureStorage:
        picture = None
        
        def __init__(self):
                return
#end

if len(sys.argv) != 2:
	print("=====ATTENTION=====")
	print("No IP specified! Defaulting to 127.0.0.1")
	print("=====ATTENTION=====")
	#exit() #UNCOMMENT when working with robot to avoid mistakes
	ip = '127.0.0.1'
else:
	ip = sys.argv[1]

print("Launched!")

camera   = camera.Camera()
storage     = PictureStorage()
network = network.Network(ip)
coordinates = coordinates.Coordinates()

def click_get_hsv(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
                hsv = worker.converttohsv(storage.picture)
                print("("+str(x)+","+str(y)+"): "+str(hsv[y][x]))

def run():
	picture = camera.tomat()
	storage.picture = picture
	cv2.imshow("Original", picture)
	cv2.setMouseCallback("Original", click_get_hsv)
	coordinates = worker.process2(picture)
	if (coordinates.found()):
		network.send(coordinates)
	
while 1==1:
	run()
	time.sleep(0.02)

cv2.destroyAllWindows()
