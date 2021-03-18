# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:12:56 2020

@author: sosboy888
"""
import sqlite3
import joblib
class AttendanceMark:
    conn=sqlite3.connect("Personnel.db")
    def __init__(self):
        pass
    def markAttendance(self,id):
        self.conn.execute("update presentee28 set presentee='Present' where id="+str(id))
        print("Presentee marked for "+str(id)+"!")
        self.conn.commit()
    def getName(self,id):
        cursor=self.conn.execute("select Name from students where id="+str(id))
        return cursor.fetchone()
    def destructor(self):
        self.conn.close()