import numpy as np 
import mahotas as mah 
import cv2
import imutils
import argparse
#imports done

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to input image")
args = vars(ap.parse_args())
#inputs parsed mazaaa aya

image = cv2.imread(args["image"])
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image,(5,5),0)


threshadapt = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,13,3)
T = mah.thresholding.otsu(image)
#this gives the value of threshold generated, do thresholding yourself
(T,thresh) = cv2.threshold(image,T,255,cv2.THRESH_BINARY_INV)

#RiddlerCalvard method too
T = mah.thresholding.rc(image)
(T,thresh2) = cv2.threshold(image,T,255,cv2.THRESH_BINARY_INV)
 
image = imutils.resize(image,width=300)
threshadapt = imutils.resize(threshadapt,width=300)
thresh = imutils.resize(thresh,width=300)
thresh2 = imutils.resize(thresh2,width=300)

stacked = np.hstack([image,threshadapt,thresh,thresh2])
cv2.imshow("threshoding",stacked)
cv2.waitKey(0)

 