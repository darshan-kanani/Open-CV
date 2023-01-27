import cv2

cap = cv2.VideoCapture("Videos/onzanimez.mp4")
# cap = cv2.VideoCapture(0)
print("Cap", cap)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (500, 700))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)
    cv2.imshow("gray",gray)
    k = cv2.waitKey(25)
    if k == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
