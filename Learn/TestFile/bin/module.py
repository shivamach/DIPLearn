#functions to be used are here
import time
import cv2

def Equalise_ColChannels(image):
	[b,g,r] = cv2.split(image)
	b = cv2.equalizeHist(b)
	g = cv2.equalizeHist(g)
	r = cv2.equalizeHist(r)
	image = cv2.merge([b,g,r])
	return image

# function equalises stuff and gives back

def counter(seconds):
	start = time.time()
	while True:
		if seconds == time.time()-start:
			return 1
		

