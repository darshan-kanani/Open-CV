import cv2
import numpy as np

def cross(x):
    pass


# blank
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow("Color Picker")

# Create switch
s1 = "0 : OFF\n1 : ON\n"
cv2.createTrackbar(s1, "Color Picker", 0, 1, cross)

# Create RGB

cv2.createTrackbar("R", "Color Picker", 0, 255, cross)
cv2.createTrackbar("G", "Color Picker", 0, 255, cross)
cv2.createTrackbar("B", "Color Picker", 0, 255, cross)


while True:
    cv2.imshow("Color Picker", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # For Exit
        break

    # Now get trackbar pos
    s = cv2.getTrackbarPos(s1, "Color Picker")
    r = cv2.getTrackbarPos("R", "Color Picker")
    g = cv2.getTrackbarPos("G", "Color Picker")
    b = cv2.getTrackbarPos("B", "Color Picker")

    if s == 0:
        img[:] = 0
    else:
        img[:] = [r, g, b]

cv2.destroyAllWindows()
