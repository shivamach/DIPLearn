import imutils
import cv2
#packages.

image = cv2.imread("jp.png")
#image is a numpy array
(h,w,d) = image.shape
#shape gives us the dimensions of image as height,width,depth
print(f"dimensions are {h}x{w}x{d}")
cv2.imshow("Image JP",image)
cv2.waitKey(0)
