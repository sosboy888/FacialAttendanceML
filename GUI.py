import Main
import PIL
from PIL import ImageTk
import PIL.Image
import cv2
from tkinter import *
from tkinter import Label
from tkinter import Tk
from tkinter import Button
from tkinter import font as tkFont
import joblib
imagesCount=joblib.load("imagesCount.sos")
root = Tk()
root.title("Facial Attendance System")
root.bind('<Escape>', lambda e: root.quit())
iconPhoto=PIL.Image.open("Images/icon.png")
icon=ImageTk.PhotoImage(iconPhoto)
resizedImage=iconPhoto.resize((100,100),PIL.Image.ANTIALIAS)
windowImage=ImageTk.PhotoImage(resizedImage)
iconLabel=Label(root,image=windowImage)
iconLabel.pack()
lmain = Label(root)
lmain.pack()
def takeSnapShot():
    global snapshot
    snapshot=True
root.iconphoto(False,icon)
textLabel=Label(root,text="Facial Attendance System, make sure you have a CUDA compatible GPU to utilize it accurately and efficiently")
textLabel.pack()
imageButton=Button(root,text="Click Photo",command=takeSnapShot)
helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)
imageButton["font"]=helv36
imageButton.config(height=60,width=60)
imageButton.pack()
snapshot=False
def show_frame():
    global imagesCount
    global snapshot
    frame = Main.processImg()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)
    if(snapshot):
        cv2.imwrite("clickedImages/"+str(imagesCount)+".jpg",frame)
        print("The image has been saved to clickedImages/"+str(imagesCount)+".jpg!")
        imagesCount=imagesCount+1
        snapshot=False
show_frame()
root.mainloop()
joblib.dump(imagesCount,"imagesCount.sos")
Main.destroy()