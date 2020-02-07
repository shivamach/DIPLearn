import numpy as np 
import cv2
import argparse
from imutils.video import VideoStream

# slow function for inverting the pixel colours this one
def invertBW(image):
	h,w = image.shape[:2]
	for i in range(w):
		for j in range(h):
			image[j,i] = 256 - image[j,i]
	return image 


ap = argparse.ArgumentParser()
ap.add_argument("-t","--type",required=True,help="Pass 1 for canny,0 for sobel")
args = vars(ap.parse_args())
choice = args["type"]
choice = int(choice)

vs = VideoStream(src=0).start()
while True:
	frame = vs.read()
	image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	if choice == 0:
		sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
		sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
		sobelX = np.uint8(np.absolute(sobelX))
		sobelY = np.uint8(np.absolute(sobelY))
		sobelCombined = cv2.bitwise_or(sobelX, sobelY)
		# sc = invertBW(sobelCombined)
		cv2.imshow("take on meeee", sobelCombined)
		key = cv2.waitKey(1)
		if key == ord('q'):
			break
	elif choice == 1:
		image = cv2.GaussianBlur(image, (5,5), 0)
		canny = cv2.Canny(image,30,150)
		# c = invertBW(canny)
		cv2.imshow("take on meeee", canny)
		key = cv2.waitKey(1)
		if key == ord('q'):
			break
	else:
		print("Invalid Type of Take on meee")


cv2.destroyAllWindows()
vs.stop()
