import numpy as np 
import cv2
#recreating imutils for self

def translate(image,x,y):
	
	M = np.float32([[1,0,x],[0,1,y]])
	shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
	return shifted

def rotate(image,angle,center=None,scale=1.0):
	(h,w) = image.shape[:2]
	if center is None:
		center = (w//2,h//2)
#angle convention is same as normal math angle convention
	M = cv2.getRotationMatrix2D(center,angle,scale)
	rotated = cv2.warpAffine(image,M,(w,h))
	return rotated
#once can resize images by rotating at a 0 angle about center	

def resize(image,width=None,height=None,scale=None,inter=cv2.INTER_AREA):
	if width is None and height is None:
		return image

	(h,w) = image.shape[:2]

	if scale is None:
		if width is None and height is not None:
			r = height/float(h)
			resized = cv2.resize(image,(int(w*r),height),interpolation=inter)
		if height is None and width is not None:
			r = width/float(w)
			resized = cv2.resize(image,(width,int(h*r)),interpolation=inter)
		if height is not None and width is not None:
			resized = cv2.resize(image,(width,height),interpolation=inter)
	else:
		w = float(w)*scale
		h = float(h)*scale
		resized = cv2.resize(image,int((w,h)),interpolation=inter)
#if scale given resize by that if not then only width or height means AR preserved scaling, for custom give no scale
#and give h and w both
	return resized				

def split_image_channels(image,show=0):
	(h,w) = image.shape[:2]
	(b,g,r)= cv2.split(image)     

	if show is 0:
		return [b,g,r]
	elif show is 1:
		buf = np.zeros((h,w,1),dtype="uint8")
		b = cv2.merge([b,buf,buf])
		g = cv2.merge([buf,g,buf])
		r = cv2.merge([buf,buf,r])
		return [b,g,r]
	else:
		print("invalid second parameter")
		print("enter either 0,1 or nothing")




