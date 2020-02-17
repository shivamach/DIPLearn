import cv2
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-m", "--mask", default="./emptyform.jpg", help="path to input mask")
ap.add_argument("-i", "--image",required=True,help="path to image which will get the mask")
args = vars(ap.parse_args())
# imports done and arguments parsed

mask = cv2.imread(args["mask"])
mask = imutils.resize(mask, width=500)
image = cv2.imread(args["image"])
image = imutils.resize(image, width=500)

output = cv2.bitwise_and(image, image , mask=mask)

cv2.imshow("output", mask)
cv2.waitKey(0)