import numpy as np 
import cv2

canvas = np.zeros((300,300,3),dtype="uint8")
#empty sheet of black as image

for i in range(0,25):
	rad = np.random.randint(0,high=200)
	r = np.random.randint(0,high=256)
	g = np.random.randint(0,high=256)
	b = np.random.randint(0,high=256)
	color = (b,g,r)
	cent1 = np.random.randint(0,high=200)
	cent2 = np.random.randint(0,high=200)
	cv2.circle(canvas,(cent1,cent2),rad,color,-1)

cv2.imshow("masterpiece",canvas)
cv2.waitKey(0)	

