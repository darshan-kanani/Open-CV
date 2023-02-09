import cv2
import numpy as np


def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (125, 0, 255), 5)

    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img, (x, y), (x+100, y+75), (125, 125, 125), 2)


cv2.namedWindow(winname="result")

img = np.zeros((512, 512, 3), np.uint8)
cv2.setMouseCallback("result", draw)

while True:
    cv2.imshow("result", img)
    if cv2.waitKey(1) & 0xFF == 27:  # esc
        break

cv2.destroyWindow()
