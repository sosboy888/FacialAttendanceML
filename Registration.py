# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:47:30 2020

@author: sosboy888
"""
import joblib
import os
import sqlite3
import tkinter
from tkinter.filedialog import askopenfilename
def main():
    count=joblib.load("count.sos")
    print("*****WELCOME TO FACE ATTENDANCE REGISTRATION!")
    print("Enter the name of the person:")
    name=input()
    count=count+1
    print("The id number of the person is:"+str(count))
    print("Please select the image file of the person:")
    tkinter.Tk().withdraw()
    imgPath=askopenfilename()
    print("The image is atimgPath)
if __name__=="__main__":
    main()