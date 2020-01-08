#!/usr/bin/env python
# coding: utf-8

# In[2]:


import imutils #image utilities
import cv2
image = cv2.imread("jp.png")
(h,w,d) = image.shape
print(f"the dimensions of image are {h}x{w}x{d}")


# In[3]:


cv2.imshow("jurrasic park",image)
cv2.waitKey(0)
#need this to make sure that image we can see otherwise it will be whoop


# In[4]:


#to access an individual pixel value
#each pixel location has a 3 tuple thingy
(b,g,r) = image[100,50] 
#co-ordinates are x=50 and y=100 for above set of pixels
#best way to remeber is that height comes first,forget x y
print(f"R={r} G={g} B={b}")


# In[5]:


#ROI is a set of values of height and width pixels 
#60,320 to 160,420
roi = image[60:160,320:420]
#roi is like subimage
cv2.imshow("ROI",roi)
cv2.waitKey(0)


# In[9]:


#resizing the image
resized = cv2.resize(image,(200,200))
cv2.imshow("rectangle",resized)
cv2.waitKey(0)


# In[6]:


#image appears squishy
#should resize with same aspect ratio
#its defined has having fixed h/w ratio
#r = h/w
dim = (300,161)
resized = cv2.resize(image,dim)
cv2.imshow("goodone",resized)
cv2.waitKey(0)


# In[7]:


resized = imutils.resize(image,width=200) # better because aspect ratio taken care
#or can also provide the target height
cv2.imshow("imutils resized",resized)
cv2.waitKey(0)


# In[10]:


#rotating an image involves - calculating interger central co-ordinates
center = (w//2,h//2)#putting width first?
M = cv2.getRotationMatrix2D(center,-45,0.5) #aboutpoint,angle,gaininsize
#obtain rotation matrix about center with angle required
rotated = cv2.warpAffine(image,M,(w,h))
#what does this do
cv2.imshow("rotated",rotated)
cv2.waitKey(0)


# In[14]:


#same image rotation is possible in one line using imutils
rotated = imutils.rotate(image,-45) #is obviously better but gain?
cv2.imshow("rotated imutils",rotated)
cv2.waitKey(0)
#imutils uses cv2, image gets clipped, a cool function of rotate bound is there which 
#the image with no clipping resizing the place


# In[15]:


rotated = imutils.rotate_bound(image,45)
#here clockwise made positive
cv2.imshow("disp",rotated)
cv2.waitKey(0)


# In[4]:


#goodpractice to blur images before doing all image processing stuff
#blurring reduces the number of high freq components
#using gaussian blue
blur = cv2.GaussianBlur(image,(11,11),0)
#11,11 is the kernel map size here. larger the kernel more the blur range of values covered
cv2.imshow("blur",blur)
cv2.waitKey(0)


# In[5]:


#drawing on an image happens on the image,work on a copy
output = image.copy()
cv2.rectangle(output,(320,60),(420,160),(0,0,255),2)
#format is fun  = img,tl,br,color,thic
cv2.imshow("rect",output)
cv2.waitKey(0)
#for text its putText(im,string,start,font,scale,color,thickness)


# In[7]:


cv2.circle(output,(300,150),20,(255,0,0),-1)
#image,center,rad,color,thickness
cv2.imshow("circle",output)
cv2.waitKey(0)


# In[ ]:




