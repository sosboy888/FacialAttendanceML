# -*- coding: utf-8 -*-
"""
Created on Tue May 26 16:25:01 2020

@author: sosboy888
"""
import face_recognition
import docopt
from sklearn import svm
import os
import joblib
def trainFaces(dir):
    encodings=[]
    ids=[]
    if(dir[-1]!="/"):
        dir+="/"
    trainingDir=os.listdir(dir)
    for id in trainingDir:
        pictures=os.listdir(dir+id)
        for picture in pictures:
            face=face_recognition.load_image_file(dir+id+"/"+picture)
            boxes=face_recognition.face_locations(face)
            if(len(boxes)==1):
                encoded=face_recognition.face_encodings(face)[0]
                encodings.append(encoded)
                ids.append(id)
            else:
                print(id+"/"+picture+" cannot be used for training.")
    classifier=svm.SVC(gamma='scale')
    classifier.fit(encodings,ids)
    joblib.dump(classifier,"trainedData.sos")
    print("Classifier Trained and Saved")
trainFaces("G:\myLab/pythonProjs/FaceAttendanceCNN/DataSet")