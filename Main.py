# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:24:23 2020

@author: sosboy888
"""
import sqlite3
import cv2
import face_recognition
from sklearn import svm
import os
import joblib
import DataExtract
import DataRecognize
recognizer=DataRecognize.Recognizer()

cam=cv2.VideoCapture(0)
while True:
    ret, img=cam.read()
    n,top_lefts,bottom_rights,ids=recognizer.faceRecognizeLive(img)
    for i in range(n):
        id=ids[i]
        cv2.rectangle(img,top_lefts[i],bottom_rights[i],[255,0,0],1)
    cv2.imshow("",img)
    if(cv2.waitKey(1)&0xFF==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()