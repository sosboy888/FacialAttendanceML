
import sqlite3
import cv2
import face_recognition
from sklearn import svm
import os
import joblib
import DataExtract
import DataRecognize
import AttendanceMarker
import dlib
print(dlib.DLIB_USE_CUDA)
recognizer=DataRecognize.Recognizer()
count=joblib.load("count.sos")
attendance=AttendanceMarker.AttendanceMark()
onlyOnce=[0 for x in range(count)]
print(count)
cam=cv2.VideoCapture(0)
while True:
    ret, img=cam.read()
    n,top_lefts,bottom_rights,ids=recognizer.faceRecognizeLive(img)
    for i in range(n):
        id=int(ids[i])
        cv2.rectangle(img,top_lefts[i],bottom_rights[i],[255,0,0],1)
        if(onlyOnce[id-1]==0):
            attendance.markAttendance(id)
            onlyOnce[id-1]=1
    cv2.imshow("",img)
    if(cv2.waitKey(1)&0xFF==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
attendance.destructor()