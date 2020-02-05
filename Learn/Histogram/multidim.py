# Redo matplotlib and come back tothis code again


import cv2
import numpy as np 
from matplotlib import pyplot as plt 
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to input image")
args = vars(ap.parse_args())
#inputs are parsed in

image = cv2.imread(args["image"])
cv2.imshow("original",image)
cv2.waitKey(0)
#display the image provided for input
chans = cv2.split(image)
fig = plt.figure()




hist = cv2.calcHist([image],[0,1,2],None,[8,8,8],[0,256,0,256,0,256])
print("3D histogram shape:{}, with {} values".format(hist.shape,hist.flatten().shape[0]))
ax = fig.add_subplot(144)
p = ax.imshow(hist,interpolation="nearest")
plt.colorbar(p)

plt.show()