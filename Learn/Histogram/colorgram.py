from matplotlib import pyplot as plt 
import cv2
import numpy as np 
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the input image")
args = vars(ap.parse_args())
#input arguments are parsed

image = cv2.imread(args["image"])
cv2.imshow("Original",image)
cv2.waitKey(0)

chans = cv2.split(image)
#splitting the channels into individual three grayscale ones
colors = ("b","g","r")
#for plotting we need to mention the color
plt.figure()
plt.title("flat color histograms")
plt.xlabel("Bins")
plt.ylabel("# of pixels")

for (chan,color) in zip(chans,colors):
	hist = cv2.calcHist([chan],[0],None,[256],[0,256])
	#each channel histogram is calculated
	plt.plot(hist,color = color)
	#plot each color one according to its color
	plt.xlim([0,256])

plt.show()	
