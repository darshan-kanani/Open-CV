import cv2
import numpy as np

def mouse_event(event,x,y,flags,param):
    font=cv2.FONT_HERSHEY_PLAIN
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,", ",y)

        cord=". "+str(x)+", "+str(y)
        cv2.putText(img,cord,(x,y),font,1,(155,125,100),2)
        # cv2.imshow("Image",img)

    elif event==cv2.EVENT_RBUTTONDOWN:
        b=img[y,x,0]
        g=img[y,x,1]
        r=img[y,x,2]

        color_bgr=". "+str(b)+", "+str(g)+", "+str(r)
        cv2.putText(img,color_bgr,(x,y),font,1,(152,255,130),2)
        # cv2.imshow("Image",img)

cv2.namedWindow(winname="result")

# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread("Images/1296932.png")
img = cv2.resize(img, (1280, 700))
cv2.setMouseCallback("result", mouse_event)

while True:
    cv2.imshow("result", img)
    if cv2.waitKey(1) & 0xFF == 27:  # esc
        break

cv2.destroyWindow()