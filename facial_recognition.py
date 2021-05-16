from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from time import strftime
from datetime import datetime
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #1st image
        img_top=Image.open("Images/face_recog1.jpg")
        img_top=img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)

        #2nd image
        img_bottom=Image.open("Images/face_recog2.jpg")
        img_bottom=img_bottom.resize((950,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)

        #button
        b1_1=Button(f_lbl,text="RECOGNIZE",command=self.recognize_attendence,cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=365,y=620,width=200,height=40)



########################################  attendance  #########################33

    def mark_attendance(self,i,n,d):
        with open("./attendance.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])

            #to avoid repeat attendance
            if( (i not in name_list) and (n not in name_list) and (d not in name_list) ):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{d},{dtString},{d1},Present")
            






########################################  face recognition  #################3
    
    def recognize_attendence(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()  
        #recognizer.read("TrainingImageLabel"+os.sep+"Trainner.yml")
        recognizer.read('./classifier.xml')
        harcascadePath = "./Cascades/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath)
        font = cv2.FONT_HERSHEY_SIMPLEX
        

        # start realtime video capture
        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cam.set(3, 640) 
        cam.set(4, 480) 
        minW = 0.1 * cam.get(3)
        minH = 0.1 * cam.get(4)

        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5,
            minSize = (int(minW), int(minH)),flags = cv2.CASCADE_SCALE_IMAGE)
            for(x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x+w, y+h), (10, 159, 255), 2)
                id,predict=recognizer.predict(gray[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host='localhost',username='root',password='abhi2021',database='face_recognition')
                my_cursor=conn.cursor()

                my_cursor.execute("select name from student_detail where student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                # my_cursor.execute("select s from student where Student_id="+str(id))
                # r=my_cursor.fetchone()
                # r="+".join(r)

                my_cursor.execute("select dep from student_detail where student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)


                my_cursor.execute("select eno from student_detail where student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                        
                if confidence>77:
                    cv2.putText(im,f"ID:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(im,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(im,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,n,d)                
                else:
                    cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(im,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)


            cv2.imshow("Welcome to Face Recognition",im)
    
            if (cv2.waitKey(1) == ord('q')):
                break
        
        cam.release()
        cv2.destroyAllWindows()













if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
