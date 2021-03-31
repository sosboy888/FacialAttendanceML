import cv2
import joblib
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
def processImg():
    ret, img=cam.read()
    scale_percent = 150
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_NEAREST)
    n,top_lefts,bottom_rights,ids=recognizer.faceRecognizeLive(resized)
    for i in range(n):
        id=int(ids[i])
        if(onlyOnce[id-1]==0):
            attendance.markAttendance(id)
            name=attendance.getName(id)
            onlyOnce[id-1]=1
        else:
            name=attendance.getName(id)
        cv2.rectangle(resized,top_lefts[i],bottom_rights[i],[255,0,0],1)
        try:
            print(name[i]+" Detected")
            img=cv2.putText(resized,str(name[i]),(top_lefts[i][0],top_lefts[i][1]-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1,cv2.LINE_AA)
        except TypeError:
            print("TYPEERROR OCCURING")
        except IndexError:
            print("INDEXERROR OCCURING")
    return resized
def destroy():
    cam.release()
    cv2.destroyAllWindows()
    attendance.destructor()