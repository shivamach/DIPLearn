# this is the outer script that will use data and bin stuff
# I think we dont need any imports here

from bin import module
from imutils.video import VideoStream
import cv2


vs = VideoStream(src=0).start()

while True:
	frame = vs.read()
	#frame = module.Equalise_ColChannels(frame)
	cv2.imshow("frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# print("STAY STILL BOI")
	if key == ord('q'):
		break
