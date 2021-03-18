# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 12:35:00 2020

@author: Intal
"""

import numpy as np
import cv2
 
face_classifier = cv2.CascadeClassifier('cascade.xml')
img = cv2.imread('hmm.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_classifier.detectMultiScale(gray, 1.05, 3)
# When no faces detected, face_classifier returns and empty tuple
if faces is ():
    print("No Face Found")
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(127,0,255),2)
    cv2.imshow('img',img)
    cv2.waitKey(0)
    
cv2.destroyAllWindows()