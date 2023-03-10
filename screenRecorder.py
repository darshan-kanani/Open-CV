import cv2 as c
import pyautogui as p
import numpy as np

# Create Resolutions
rs = p.size()

# filename in which we store recording
fn = input("Enter Any File Name And Path : ")
# fix the frame rate
fps = 30.0

# fourcc = c.VideoWriter_fourcc(*'XVID')
fourcc = c.VideoWriter_fourcc('m', 'p', '4', 'v')
output = c.VideoWriter(fn, fourcc, fps, rs)

# creating recording module
c.namedWindow("Live_Recording", c.WINDOW_NORMAL)
# c.resize("Live_Recording", (600, 400))

while True:
    img = p.screenshot()
    f = np.array(img)
    f = c.cvtColor(f, c.COLOR_BGR2RGB)
    output.write(f)
    c.imshow("Live_Recording", f)
    if c.waitKey(1) == ord("q"):
        break

output.release()
c.destroyAllWindows()
