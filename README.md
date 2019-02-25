 ## First examples in CV
 ## 第一个案例
 * loading picture
 * loading video data


 ## Show Image Example
 ## 显示图片
``` python
import cv2
import numpy as np

img = cv2.imread("girl.jpg",0)
height, width = img.shape
cv2.imshow("Hello World",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```


 ## Cam Example
 ## 加载摄像头
``` python
# use computer
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,1080)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,720)

while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow(" Video example exit by 'q' ", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()

cv2.destroyAllWindows() 
```


## CVUI
A (very) simple UI lib built on top of OpenCV drawing primitives. Other UI libs, such as imgui, require a graphical backend (e.g. OpenGL) to work, so if you want to use imgui in a OpenCV app, you must make it OpenGL enabled, for instance. It is not the case with cvui, which uses only OpenCV drawing primitives to do all the rendering (no OpenGL or Qt required).

--
## UI example
```python
import numpy as np
import cv2
import cvui

WINDOW_NAME = 'CVUI Test'

cvui.init(WINDOW_NAME)
frame = np.zeros((200, 400, 3), np.uint8)

while True:
    frame[:] = (49, 52, 49)
    cvui.text(frame, 10, 15, 'Hello world!')

    # Update cvui internal stuff
    cvui.update()

    # Show window content
    cv2.imshow(WINDOW_NAME, frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
		break
```
