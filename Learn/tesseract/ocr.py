from PIL import Image
import pytesseract
import argparse
import cv2
import os
# imports

# parsing arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True, help="Path to input image")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",help="type of preprocessing to be done")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# add a pre-processing that is more advanced for better image results 
# and such

if args["preprocess"] == "thresh":
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)

filename = "{}.png".format(os.getpid())
# pid process id to get a random name for image
cv2.imwrite(filename, gray)

text = pytesseract.image_to_string(Image.open(filename))
# open image in PIL form to use tesseract
os.remove(filename)
# delete the temporary created image
print(text)

cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)