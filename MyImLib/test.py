import imlibmy as im
import cv2

image = cv2.imread("test.jpg")

[b,g,r] = im.split_image_channels(image,1)

cv2.imwrite("blue.jpg",b)
cv2.imwrite("green.jpg",g)
cv2.imwrite("red.jpg",r)