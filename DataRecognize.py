
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
        id=-1
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
            imgEncoding=face_recognition.face_encodings(img,model="small")[i]
            id=self.classifier.predict([imgEncoding])
            print(*id)
        cv2.imshow("Faces",image)
        cv2.waitKey(0)
        cv2.destroyWindow("Faces")
        return id
    def faceRecognizeLive(self,img):
        id=-1
        faces=face_recognition.face_locations(img,model="cnn")
        top_lefts=[]
        bottom_rights=[]
        ids=[]
        for face in faces:
            top_left=(face[3],face[0])
            top_lefts.append(top_left)
            bottom_right=(face[1],face[2])
            bottom_rights.append(bottom_right)
        number=len(faces)
        print("Number of faces detected="+str(number))
        allEncodings=face_recognition.face_encodings(img,known_face_locations=faces)
        for i in range(number):
            imgEncoding=allEncodings[i]
            id=self.classifier.predict([imgEncoding])
            ids.append(*id)
            print(*id)
            print("Confidence obtained:"+str(self.classifier.score([imgEncoding],[id])*100))
        return len(faces),top_lefts,bottom_rights,ids