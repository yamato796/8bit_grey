from time import time
from io   import BytesIO
from tqdm import tqdm
#import datetime
import os 
import cv2
import math
import numpy as np
import base64
import logging
import random
# grey depth scale--------original size if both set to 255 
length = 100
# actual size of the image
size = length*length*2

img = np.ones((size,size,1),np.uint8)
#-----------x, y be manual moving position-------
x =0
y =0

for i in tqdm(range(0,length)):
	for j in range(0,length):
		for k in range(0,length):
			for l in range(0,length):
				img[x  ][y  ] = i*(255/length)
				img[x+1][y  ] = j*(255/length)
				img[x  ][y+1] = k*(255/length)
				img[x+1][y+1] = l*(255/length)
				if x < size-2:
					x=x+2
				elif y< size-2:
					x=0
					y=y+2

cv2.imwrite("./img_{0}.tiff".format(length),img)
