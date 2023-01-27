import cv2

cap = cv2.VideoCapture("Videos\\onzanimez.mp4")
print("Cap", cap)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (500, 700))
    cv2.imshow("frame", frame)
    k = cv2.waitKey(25)
    if k == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
