#Written in python 2.7 and uses OpenCV 2.1
import cv2.cv as cv
import time
import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:    
    ret, frame = cap.read()
    frame = cv2.blur(frame,(3,3))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    thresh = cv2.inRange(hsv,np.array((0, 80, 80)), np.array((20, 255, 255)))

    #cv2.imshow('frame',frame)

    thresh2 = thresh.copy()

    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0
    best_cnt = 1
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>max_area:
            max_area = area
            best_cnt = cnt
    M = cv2.moments(best_cnt)
    cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    cv2.circle(frame,(cx,cy),10,255,-1)

    cv2.imshow('frame',frame)
    cv2.imshow('thresh',thresh2)

    if cv.WaitKey(10) == 27:
        break 