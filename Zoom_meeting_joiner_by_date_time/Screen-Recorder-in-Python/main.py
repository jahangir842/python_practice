
import sys
# sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
import numpy as np
import pyautogui    # Install using "pip install pyautogui"
import time
from PIL import ImageGrab


# sys.path.append('/usr/local/lib/python2.7/site-packages')
SCREEN_SIZE = (1366, 768)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

# out = cv2.VideoWriter('filename.avi',
#                              cv2.VideoWriter_fourcc(*'MJPG'),
#                              10, SCREEN_SIZE)

delay = 60*60 # For 60 minutes delay
close_time = time.time()+delay

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)



    out.write(frame)
    print("writing output ")
    # cv2.imshow('Frame', frame)
    for image in frame:
        # cv2.resizeWindow('recording', 1000, 1000)
        image = cv2.resize(image, (960, 540))
        cv2.imshow("recording", image)

    if time.time() > close_time:
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
out.release()
