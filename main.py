from time import time
from io   import BytesIO

import os 
import cv2
import math
import numpy as np
import base64
import logging
import random


x =0
y =0
img = np.zeros((131072,131072,1),np.uint8)
for i in range(0,255):
	for j in range(0,255):
		for k in range(0,255):
			for l in range(0,255):
				img[x  ][y  ] = i
				img[x+1][y  ] = j
				img[x  ][y+1] = k
				img[x+1][y+1] = l
				if x <131070:
					x=x+2
				else:
					x=0
					y=y+2

cv2.imwrite("./img.png",img)
