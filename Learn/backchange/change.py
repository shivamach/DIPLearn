# imports
import cv2
import numpy as np

image = cv2.imread("image.jpg")
(h, w) = image.shape[:2]
cv2.imshow("ol", image)
cv2.waitKey(0)
count = 0
for i in range(h):
    for j in range(w):
        k = image[i, j]
        if k.all() == np.array([212, 100, 0]).all():
            image[i, j] = np.array([255, 255, 255])
            count = count + 1
        else:
            print(count)

cv2.imshow("new", image)
cv2.waitKey(0)
