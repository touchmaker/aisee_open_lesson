import numpy as np
import cv2
import cvui

WINDOW_NAME = 'CVUI CheckBox Example'

cvui.init(WINDOW_NAME)
frame = np.zeros((200, 400, 3), np.uint8)

# use an array/list because this variable will be changed by cvui
checkboxState = [True]

while True:
    frame[:] = (49, 52, 49)

    # Render the checkbox. Notice that checkboxState is used AS IS,
    # e.g. simply "checkboxState" instead of "checkboxState[0]".
    # Only internally that cvui will use checkboxState[0].
    cvui.checkbox(frame, 10, 15, 'checkbox', checkboxState)

    cvui.update()
    
    cv2.imshow(WINDOW_NAME, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break