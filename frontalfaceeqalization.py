# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 18:27:00 2021

@author: gauri
"""

import cv2
video_capture = cv2.VideoCapture(0)
while(1):
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    r,g,b=cv2.split(frame)
    R = cv2.equalizeHist(r)
    G = cv2.equalizeHist(g)
    B = cv2.equalizeHist(b)
    imgm=cv2.merge((R,G,B))    
    # Display the resulting frame
    cv2.imshow('Video', frame)
    cv2.imshow('Equilize', imgm)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()