from time import time
from io   import BytesIO

#import datetime
import os 
import cv2
import math
import numpy as np
import base64
import logging
import random

#img = np.ones((65536,65536,1),np.uint8)
length = 32
width = 32
size_x = length*length*2
size_y = width*width*2
img = np.ones((size_x,size_y,1),np.uint8)
#img*=255
x =0
y =0
#img = np.zeros((131072,131072,1),np.uint8)
for i in range(0,length):
	for j in range(0,length):
		for k in range(0,length):
			for l in range(0,length):
				print x,y
				img[x  ][y  ] = i*(255/length)
				img[x+1][y  ] = j*(255/length)
				img[x  ][y+1] = k*(255/length)
				img[x+1][y+1] = l*(255/length)
				if x < size_x-2:
					x=x+2
				elif y< size_y-2:
					x=0
					y=y+2

cv2.imwrite("./img2.png",img)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
