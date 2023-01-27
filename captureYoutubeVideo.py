import cv2
import pafy

url="https://www.youtube.com/watch?v=giccudEmap4&ab_channel=creimamkf"
data=pafy.new(url)
data=data.getbest(preftype="mp4")
cap = cv2.VideoCapture(0)

cap.open(data.url)

# # XVID,DIVX,MJPG,X264,WMV1,WMV2 Video Formats
# fourcc=cv2.VideoWriter_fourcc(*"XVID")
#                         # name,                 codec, fps,resolution
# output=cv2.VideoWriter("OutputVideo/output.mp4",fourcc,20.0,(640,480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.resize(frame, (700, 700))
        # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame)
        # cv2.imshow("gray",gray)
        # output.write(frame)
        if cv2.waitKey(1) == ord("q"):
            break

cap.release()
# output.release()
cv2.destroyAllWindows()
