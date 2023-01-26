import cv2

path = input("Enter The Path Of Image : ")
print("Your Entered Path Is : ", path)

img = cv2.imread(path, 0)
img = cv2.resize(img, (1280, 720))
# img=cv2.flip(img,0)

cv2.imshow("Coverted Image", img)
k = cv2.waitKey(0)

if k == ord("s"):
    cv2.imwrite("OutputImages/Output.png", img)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()
