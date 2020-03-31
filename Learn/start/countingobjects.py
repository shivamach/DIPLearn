#!/usr/bin/env python
# coding: utf-8

# In[2]:


import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to input image")
args = vars(ap.parse_args())
#this is useful for providing extra information to the program at runtime from terminal
#args["image"] refers to the path to the image now onwards in the code


# In[3]:


import imutils
import cv2

image = cv2.imread("tetris_blocks.png")
cv2.imshow("original image",image)
cv2.waitKey(0)
#taking image in image variable

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#cvtColor used, image and then the function for conversion in cv2
cv2.imshow("grey",gray)
cv2.waitKey(0)


# In[4]:


#edge detection
edged = cv2.Canny(gray,30,150)
#inputs are gray image,threshold min,max and aperture_size = kernel,default is 3
cv2.imshow("Edged",edged)
cv2.waitKey(0)


# In[9]:


#thresholding
#done to remove lighter or darker regions
thresh = cv2.threshold(gray,225,255,cv2.THRESH_BINARY_INV)[1]
#input image,threshold,setto,
#here all pixels with value above 225 are set to 0 and below to 255,last parameter makes it happen
thresh2 = cv2.threshold(gray,225,255,cv2.THRESH_BINARY)[1]
#see what happens to this image makes sense
cv2.imshow("Thresh",thresh)
cv2.waitKey(0)
cv2.imshow("Thresh2",thresh2)
cv2.waitKey(0)
#https://docs.opencv.org/3.4.0/d7/d1b/group__imgproc__misc.html#ggaa9e58d2860d4afa658ef70a9b1115576a19120b1a11d8067576cc24f4d2f03754


# In[17]:


#to detect and draw contours,thresholding is necessary
cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#input image is thresholded , read about the parameters extra
cnts = imutils.grab_contours(cnts)
#makes up for function differences over different opencv versions
output = image.copy()

for c in cnts:
    cv2.drawContours(output,[c],-1,(240,0,159),3)
    cv2.imshow("contours",output)
    cv2.waitKey(0)
#for counting the number of contours we can use len(cnts)


# In[12]:


#Erosions and Dilations,to reduce noise in the binary images
#set foreground to white for following code
mask = thresh.copy()
mask = cv2.erode(mask,None,iterations=5)
#iterations is the number otf times the mask runs over the image
cv2.imshow("er",mask)
cv2.waitKey(0)


# In[15]:


mask2 = thresh.copy()
mask2 = cv2.dilate(mask,None,iterations=5)
cv2.imshow("Dilated",mask)
cv2.waitKey(0)


# In[20]:


#masking and bitwise operations
#using the thresholded image as a mask
mask = thresh.copy()
output = cv2.bitwise_and(image,image,mask=mask)
#mask is the thresh image copy
#output,input,mask=maskimagename
cv2.imshow("masked",output)
cv2.waitKey(0)


# In[ ]:




