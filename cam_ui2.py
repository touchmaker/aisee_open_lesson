import numpy as np 
import cv2
import cvui

WINDOW_NAME	= 'Threshold Camera'

chooseArr = [cv2.THRESH_BINARY,cv2.THRESH_BINARY_INV,cv2.THRESH_TRUNC,cv2.THRESH_TOZERO ,cv2.THRESH_TOZERO_INV]
strArr = ["THRESH_BINARY","THRESH_BINARY_INV","THRESH_TRUNC","THRESH_TOZERO","THRESH_TOZERO_INV"]

def main():
	thresholdValue = [108]
	chooseInt = [0]

	# Size of trackbars
	trackbar_width = 400

	#init cvui
	cvui.init(WINDOW_NAME, 20)
	ui_frame = np.zeros((480, 640, 3), np.uint8)

	#camera setting
	cap = cv2.VideoCapture(0)
	cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,640)
	cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,480)

	#main loop
	while (True):
		ret, frame = cap.read()
		
		#print frame.dtype
		#to gray
		gray = cv2.cvtColor( frame ,cv2.COLOR_BGR2GRAY)
		
		ui_frame[:] = (49, 52, 49)
		cvui.beginColumn(ui_frame, 20, 20, -1, -1, 6)
		
		cvui.text('Threshold Adject')
		cvui.trackbar(trackbar_width, thresholdValue, 0, 255)

		cvui.counter(chooseInt);

		cvui.space(5)

		cvui.text(strArr[chooseInt[0]])

		if cvui.button('&Quit'):
			break

		cvui.space(5)

		cvui.endColumn()

		th1,gray = cv2.threshold(gray, thresholdValue[0], 255, chooseArr[chooseInt[0]])
		merged = cv2.merge([gray ,gray ,gray])

		dst = cv2.addWeighted(ui_frame,1.0,merged ,0.4,0.0)

		cvui.update()

		cv2.imshow(WINDOW_NAME, dst)

	cap.release()
	cv2.destroyAllWindows() 

if __name__=='__main__':
	main()


