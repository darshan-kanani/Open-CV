import cv2 as c
import pyautogui as p
import numpy as np

# Create Resolutions
rs = p.size()

# filename in which we store recording
fn = input("Enter Any File Name And Path : ")
# fix the frame rate
fps = 30.0

fourcc = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter(fn, fourcc, fps, rs)

# creating recording module
c.namedWindow("Live_Recording",c.WINDOW_NORMAL)
c.resize("Live_Recording",(600,400))

while True:
    img=p.screenshot()
    f=np.array()