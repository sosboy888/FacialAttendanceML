# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:43:54 2020

@author: sosboy888
"""

import cv2
cam=cv2.VideoCapture(0)
while True:
    ret,img=cam.read()
    cv2.imshow("",img)
    if(cv2.waitKey(1)&0xFF==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()