import numpy as np 
import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to image")
args = vars(ap.parse_args())
#arguments parsed

image = cv2.imread(args["image"])
image = imutils.resize(image, width=640)
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

lap = cv2.Laplacian(image, cv2.CV_64F)
'''
gives gradient image tracking changes from b2w and w2b, w2b has negative slope
hence using 64 float and not our usual unsigned int 8 bit.
next we shall calculate absoulute values and converted gradient float back into 
numpy array of unint8 to see it as an image
'''
lap = np.uint8(np.absolute(lap))
cv2.imshow("DekhBC", np.hstack([image,lap]))
cv2.waitKey(0)
