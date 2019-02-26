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
 

 ### 针对非MS Microsoft VisualStudio 的方法 比如MAC
 * install python 2.6 
 * install cv2 numpy matplotlib cvui
 
  ``` powershell
pip install --upgrade setuptools
pip install matplotlib
pip install numpy
pip install opencv-python==版本号
 ```
---
*  Via pip you can specify the package version to install using the following: 指定版本号
 
``` bash
pip install opencv-python==2.4.9
```
However, that package does not seem to be available on pypi.
A little trick for checking available versions:

``` bash
pip install opencv-python==
``` 
Which returns:
Could not find a version that satisfies the requirement opencv-python== 
(from versions: 3.1.0.0, 3.1.0.1, 3.1.0.2, 3.1 .0.3, 3.1.0.5, 3.2.0.6, 3.2.0.7) 

---

 ## 安装 Visual Studio 2017 Community

  ### 目前仅在 Visual Studio for Windows 中提供 Python 支持；在 Mac 和 Linux 上，可通过 Visual Studio Code 获取 Python 支持。
下载并运行适用于 Windows 的最新 Visual Studio 2017 安装程序（版本 15.2 及更高版本提供 Python 支持）。 如果已安装 Visual Studio，请运行 Visual Studio 安装程序

   ### 提示
  Community Edition 适用于个体开发者、课堂学习、学术研究和开放源代码开发。 对于其他用途，请安装 Visual Studio 2017 Professional 或 Visual Studio 2017 Enterprise。
 
 ---
 
  ### 对于 Python，请选择 Python 开发工作负载，然后选择“安装”：

  ### 若要快速测试 Python 支持，请启动 Visual Studio，按 Alt+I 打开 Python 交互窗口，然后输入
  ``` python
  2+2
  ``` 
  
  ### 如果看不到输出 4，请重新检查步骤。

 ---
  ###  安装包教程
 https://docs.microsoft.com/zh-cn/visualstudio/python/tutorial-working-with-python-in-visual-studio-step-05-installing-packages?view=vs-2017
 ---
 
  ### 测试安装是否成功环境 在Python环境
* test code
 ``` python 
 import cv2
 print cv2.CV_AA
```

 ---
 
 ## First examples in CV
 ## 入门案例
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
# 使用matplotlib
```python
import numpy as np 
import cv2 
from matplotlib import pyplot as plt 
 
img = cv2.imread('messi5.jpg',0) 
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic') 
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis 
plt.show()
```


---
# Homework
# 作业

创建一个可以显示摄像头内容的窗体，在窗体内部放置一个checkbox，通过checkbox 来改变图形的性质
比如颜色图像或黑白图像


---

# Fin

---
