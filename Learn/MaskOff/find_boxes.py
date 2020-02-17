import cv2
import numpy as np 
import argparse
import imutils
# import done

def sort_contours(cnts, method="left-to-right"):
	# initialize the reverse flag and sort index
	reverse = False
	i = 0
	# handle if we need to sort in reverse
	if method == "right-to-left" or method == "bottom-to-top":
		reverse = True
	# handle if we are sorting against the y-coordinate rather than
	# the x-coordinate of the bounding box
	if method == "top-to-bottom" or method == "bottom-to-top":
		i = 1
	# construct the list of bounding boxes and sort them from top to
	# bottom
	boundingBoxes = [cv2.boundingRect(c) for c in cnts]
	(cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
		key=lambda b:b[1][i], reverse=reverse))
	# return the list of sorted contours and bounding boxes
	return (cnts, boundingBoxes)



ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="path to input image")
args = vars(ap.parse_args())
# arguments parsed

img = cv2.imread(args["image"])
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = imutils.resize(img, width=500)
# thresholding the image
(thresh, img_bin) = cv2.threshold(img, 215, 255, cv2.THRESH_BINARY)
img_bin = 255-img_bin

# detecting boxes using morphological operations
kernel_length = np.array(img).shape[1]//80

# vertical kernel
vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,kernel_length))

# horizontal kernel
hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length,1))

# a kernel of 3*3 ones
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# kernels defined

# apply the morphological shits
img_temp1 = cv2.erode(img_bin, vertical_kernel, iterations=3)
vertical_lines_img = cv2.dilate(img_temp1, vertical_kernel, iterations=3)

img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=3)
horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=3)

# add the images together
alpha = 0.5
beta = 1.0 - alpha

img_final_bin = cv2.addWeighted(vertical_lines_img, alpha, horizontal_lines_img, beta, 0.0)
img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)
# img_final_bin = cv2.cvtColor(img_final_bin, cv2.COLOR_BGR2GRAY)
(thresh, img_final0) = cv2.threshold(img_final_bin, 210, 255, cv2.THRESH_BINARY)



# Find contours for image, which will detect all the boxes
contours, hierarchy = cv2.findContours(img_final0, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Sort all the contours by top to bottom.
(contours, boundingBoxes) = sort_contours(contours, method="top-to-bottom")

idx = 0
for c in contours:
    # Returns the location and width,height for every contour
    x, y, w, h = cv2.boundingRect(c)
    if (w > 80 and h > 20) and w > 3*h:
        idx += 1
        new_img = img[y:y+h, x:x+w]
        cv2.imwrite("./output/img"+str(idx)+ '.png', new_img)# If the box height is greater then 20, widht is >80, then only save it as a box in "cropped/" folder.


# add two images with some weight and then display the sum
cv2.imwrite("mask.jpg", img_final_bin)
second = cv2.imread("./test2.jpg")
cv2.imshow("detected lines", img_final_bin)
cv2.waitKey(0)

