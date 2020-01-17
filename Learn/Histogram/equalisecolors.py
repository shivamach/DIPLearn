#histogram equalisation is carried out for grayscale images.
#Wish to equalise all colors and see what goes down

import numpy as np 
import cv2
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the input file image")
args = vars(ap.parse_args())
#input argumentsa are parsed

image = cv2.imread(args["image"])

[b,g,r] = cv2.split(image)

b = cv2.equalizeHist(b)
g = cv2.equalizeHist(g)
r = cv2.equalizeHist(r)
image2 = cv2.merge([b,g,r])
#each color equalised seperately and merged to get equalised image
cv2.imshow("histogramequalisation",np.hstack([image,image2]))
cv2.waitKey(0)
#WORKS REALLy well for images where lighting is abundant in forground and background both