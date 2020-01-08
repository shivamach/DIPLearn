import imutils
import cv2
import numpy as np
image = cv2.imread("pink.jpg")
#input image

bounds = [
([150,10,10],[255,60,60]),
([10,150,10],[60,255,60]),
([10,10,150],[60,60,255]),
]
#color boundary values trying out for seperating bgr
(h,w,d) = image.shape

for (lower,upper) in bounds:
    lower = np.array(lower,dtype = "uint8")
    upper = np.array(upper,dtype = "uint8")
    #numpy arrays of boundaries

    mask = cv2.inRange(image,lower,upper)
    output = cv2.bitwise_and(image,image,mask=mask)

    cv2.imshow("images",output)
    cv2.waitKey(0)
    #this code can only seperate red as of now
    #the right bound values will make this quite good
    #yay it works
