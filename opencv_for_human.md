# Computer Vision for Human
# 为人写的图形图像学课程
  route for none-computer users' openCV lessons 
  with examples and source code
  
  ---
 ## 特色 Fetures
 * introdue to compter vision (cv2)
 * 介绍compter vision (cv2)
 * install cv2
 * 如何安装
 * loading pictrure/camera/movie
 * 加载图片和摄像头或视频问价
 * cvui for cv
 * 简单的图形界面 cvui
 * Picture correction methods
 * 图片透视校正
 * Table/grid's data fetch
 * 表格数据榨取

 ---
 
 ##  5 minutes introduction of compter vision (cv2)
 ## 5 分钟快速上手教程
 
 ---

 ## Install
 ## 安装

 ### for MAC or Linux 
 ### 针对MAC或LINUX系统
 * install python 2.6 for example
 * install cv2 with pip
 
  ``` powershell
pip install --upgrade setuptools
pip install opencv-python
 ```

 #### for Microsoft VisualStudio 2013 +
 #### 针对WIN64系统
 * 仅需要安装 Python 和 opencv 包
 
## 测试安装是否成功环境 在Python环境
* test code
 ``` python 
 import cv2
 print cv2.CV_AA
```
 
 ---
 
 ## First examples in CV
 ## 第一个案例
 * loading picture
 * loading video data

---

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

---

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

---

## CVUI
A (very) simple UI lib built on top of OpenCV drawing primitives. Other UI libs, such as imgui, require a graphical backend (e.g. OpenGL) to work, so if you want to use imgui in a OpenCV app, you must make it OpenGL enabled, for instance. It is not the case with cvui, which uses only OpenCV drawing primitives to do all the rendering (no OpenGL or Qt required).

---
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

* NOTES change code CV2_LINE to CV_AA

---
# Homework 1
# 作业

创建一个可以显示摄像头内容的窗体，在窗体内部放置一个checkbox，通过checkbox 来改变图形的性质
比如颜色图像或黑白图像


---

# Fin

---
