import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,1080)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,720)

while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture exit by 'q'", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()

cap.release()
cv2.destroyAllWindows() 
