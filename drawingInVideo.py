import cv2
import datetime

cap = cv2.VideoCapture("Videos\\onzanimez.mp4")

while (cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (500, 700))
    if ret == True:
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        text = 'Height : '+str(cap.get(4))+' Width : '+str(cap.get(3))
        frame = cv2.putText(frame, text, (10, 20), font, 1,
                            (0, 155, 255), 1, cv2.LINE_AA)

        date_date = "Date : "+str(datetime.datetime.now())
        frame = cv2.putText(frame, date_date, (20, 50), font, 1,
                            (0, 155, 255), 1, cv2.LINE_AA)

        cv2.imshow('frame', frame)

        if cv2.waitKey(30) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
