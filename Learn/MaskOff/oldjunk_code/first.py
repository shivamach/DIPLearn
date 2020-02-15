import argparse
import cv2
import numpy as np 
import imutils
# imports

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to image to be processed")
args = vars(ap.parse_args())
# arguments parsed

image = cv2.imread(args["image"])
image = imutils.resize(image, width=600)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3,3), 0)
edged = cv2.Canny(blurred, 30, 160)
backup_edged = 255-edged
contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


cv2.imshow("window",np.hstack([gray,img]))
cv2.waitKey(0)
