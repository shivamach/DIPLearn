import numpy as np 
import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to image")
args = vars(ap.parse_args())
#arguments parsed

image = cv2.imread(args["image"])
image = imutils.resize(image, width=500)
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)
#smart

cv2.imshow("Done,Boii",np.hstack([image,sobelX,sobelY,sobelCombined]))
cv2.waitKey(0)