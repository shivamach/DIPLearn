import cv2
import numpy as np
import argparse 
from matplotlib import pyplot as plt 
#importing necessay libraries

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Pass the image for histogram construction")

args = vars(ap.parse_args())
#input arguments are parsed now

image = cv2.imread(args["image"])
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#grayscale histogram wants the grayscale image

hist = cv2.calcHist([image],[0],None,[256],[0,256])
#the format is 
#

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("bins")
plt.ylabel("# of pixels")
plt.plot(hist)

plt.xlim([0,256])
plt.show()
cv2.waitKey(0)