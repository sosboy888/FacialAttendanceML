
import face_recognition
import docopt
from sklearn import svm
import os
import joblib
def trainFaces(dir):
    encodings=[]
    ids=[]
    count=0
    imagesCount=joblib.load("imagesCount.sos")
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
        count=count+1
    classifier=svm.SVC(gamma="auto")
    classifier.fit(encodings,ids)
    joblib.dump(classifier,"trainedData.sos")
    joblib.dump(count,"count.sos")
    joblib.dump(imagesCount,"imagesCount.sos")
    print("Classifier Trained and Saved")
#The path to your dataset folder
trainFaces("G:\myLab\pythonProjs\FaceAttendanceCNN\DataSet")