import numpy as np
import cv2

img = cv2.imread("Images\\1296932.png")
img = cv2.resize(img, (1000, 800))

# img = np.zeros([512, 512, 3], np.uint8)*255  # For white screen
# img = np.ones([512, 512, 3], np.uint8)*255  # create window of an black screen

# Here line accept 5 parameter (img,starting,ending,color,thickness)
img = cv2.line(img, (0, 0), (200, 200), (154, 92.4), 2)

# arrowed line accept also accpet 5 parameter  (img,starting,ending,color,thickness)
img = cv2.arrowedLine(img, (0, 125), (255, 255), (15, 192, 42), 2)

# Rectangle - accept parameter(img,start_co,end_co,colot ,thickness)
img = cv2.rectangle(img, (384, 10), (510, 128), (128, 0, 255), 2)

# circle - accept(img,star_co,radius,color,thickness)
img = cv2.circle(img, (447, 125), 63, (214, 255, 0), 2)

font = cv2.FONT_ITALIC
# puttext -accept(img,text,start_co,font,fontsize,color,thickness,linetype)
img = cv2.putText(img, "LAW", (20, 500), font, 4,
                  (0, 125, 255), 2, cv2.LINE_AA)

# ellipse-accept(img,start_cor,(length,height),color,thickness)
img = cv2.ellipse(img, (400, 600), (100, 50), 0, 0, 270, 155, 2)

cv2.imshow("output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
