# -*- coding: utf-8 -*-
"""
Created on Tue May 26 16:58:01 2020

@author: sosboy888
"""

import face_recognition
import docopt
from sklearn import svm
import os
import cv2
import joblib
class Recognizer:
    classifier=joblib.load("trainedData.sos")
    def __init__(self):
        pass
    def faceRecognize(self,imgPath):
        img=face_recognition.load_image_file(imgPath)
        faces=face_recognition.face_locations(img)
        image=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        for face in faces:
            top_left=(face[3],face[0])
            bottom_right=(face[1],face[2])
            color=[255,0,0]
            cv2.rectangle(image,top_left,bottom_right,color,1)
        number=len(faces)
        print("Number of faces detected="+str(number))
        for i in range(number):
            imgEncoding=face_recognition.face_encodings(img)[i]
            id=self.classifier.predict([imgEncoding])
            print(*id)
        cv2.imshow("Faces",image)
        cv2.waitKey(0)
        cv2.destroyWindow("Faces")
Recognizer().faceRecognize("1.png")