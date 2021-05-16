from tkinter import*
import tkinter
from tkinter import ttk  #Containes style toolkit
from PIL import Image,ImageTk  # pil-pillow
import os
from student_detail import Student
from facial_recognition import Face_Recognition
from train import Train
from attendance import Attendance
from developer import Developer
from help import Help 


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        # geometry set
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        

        img=Image.open("Images/juet guna.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg=ImageTk.PhotoImage(img)

        first_lb=Label(self.root, image=self.photoimg)
        first_lb.place(x=0,y=0,width=500,height=130)


        img1=Image.open("Images/face_recog_3.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_lb=Label(self.root, image=self.photoimg1)
        first_lb.place(x=500,y=0,width=500,height=130)


        img2=Image.open("Images/face_rec_1.jpg")
        img2=img2.resize((530,130),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_lb=Label(self.root, image=self.photoimg2)
        first_lb.place(x=1000,y=0,width=530,height=130)


        # img3=Image.open("Images/logo.jpg")
        # img3=img3.resize((130,130),Image.ANTIALIAS)   #High level img to Low level img
        # self.photoimg3=ImageTk.PhotoImage(img3)

        # first_lb=Label(self.root, image=self.photoimg3)
        # first_lb.place(x=1400,y=0,width=130,height=130)



        #Bg Image
        bg=Image.open("Images/backg2.jfif")
        bg=bg.resize((1530,710),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg_bg=ImageTk.PhotoImage(bg)

        bg_image=Label(self.root, image=self.photoimg_bg)
        bg_image.place(x=0,y=130,width=1530,height=710)


        title_lb=Label(bg_image,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("PT Serif",35,"bold"),bg="#faffc7",fg="#f7520f")
        title_lb.place(x=0,y=0,width=1530,height=50)


        #Student Button
        std_1=Image.open("Images/std_1.jpg")
        std_1=std_1.resize((220,220),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg_std_1=ImageTk.PhotoImage(std_1)

        b1=Button(bg_image,image=self.photoimg_std_1,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width =220,height=220)

        b1_txt=Button(bg_image,text="Student Details",command=self.student_details,cursor="hand2",font=("PT Serif",15,"bold"),bg="#040229",fg="white")
        b1_txt.place(x=200,y=300,width =220,height=40)


        #Detect Face
        face_1=Image.open("Images/face_detect.jpg")
        face_1=face_1.resize((220,220),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg_face=ImageTk.PhotoImage(face_1)

        b1=Button(bg_image,image=self.photoimg_face,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width =220,height=220)

        b1_txt=Button(bg_image,text="Face Recognizer",command=self.face_data,cursor="hand2",font=("PT Serif",15,"bold"),bg="#040229",fg="white")
        b1_txt.place(x=500,y=300,width =220,height=40)



        #Attendance 
        att=Image.open("Images/att.png")
        att=att.resize((220,220),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg_att=ImageTk.PhotoImage(att)

        b1=Button(bg_image,command=self.attendance_data,image=self.photoimg_att,cursor="hand2")
        b1.place(x=800,y=100,width =220,height=220)

        b1_txt=Button(bg_image,text="Attendance",command=self.attendance_data,cursor="hand2",font=("PT Serif",15,"bold"),bg="#040229",fg="white")
        b1_txt.place(x=800,y=300,width =220,height=40)


        #Help Desk
        help=Image.open("Images/help_d.jpg")
        help=help.resize((220,220),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg_help=ImageTk.PhotoImage(help)

        b1=Button(bg_image,image=self.photoimg_help,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width =220,height=220)

        b1_txt=Button(bg_image,text="Help Desk",command=self.help_data,cursor="hand2",font=("PT Serif",15,"bold"),bg="#040229",fg="white")
        b1_txt.place(x=1100,y=300,width =220,height=40)


        #Training the algo
        train=Image.open("Images/training.jpg")
        train=train.resize((220,220),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg_train=ImageTk.PhotoImage(train)

        b1=Button(bg_image,image=self.photoimg_train,command=self.train_data,cursor="hand2")
        b1.place(x=200,y=380,width =220,height=220)

        b1_txt=Button(bg_image,text="Training data",command=self.train_data,cursor="hand2",font=("PT Serif",15,"bold"),bg="#040229",fg="white")
        b1_txt.place(x=200,y=580,width =220,height=40)


        #Data library
        photos=Image.open("Images/store.jpg")
        photos=photos.resize((220,220),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg_photos=ImageTk.PhotoImage(photos)

        b1=Button(bg_image,command=self.open_img,image=self.photoimg_photos,cursor="hand2")
        b1.place(x=500,y=380,width =220,height=220)

        b1_txt=Button(bg_image,command=self.open_img,text="Image Library",cursor="hand2",font=("PT Serif",15,"bold"),bg="#040229",fg="white")
        b1_txt.place(x=500,y=580,width =220,height=40)


        #Developer info/Contact
        Dev=Image.open("Images/dev1.jpg")
        Dev=Dev.resize((220,220),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg_Dev=ImageTk.PhotoImage(Dev)

        b1=Button(bg_image,image=self.photoimg_Dev,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width =220,height=220)

        b1_txt=Button(bg_image,text="Contact Developer",command=self.developer_data,cursor="hand2",font=("PT Serif",15,"bold"),bg="#040229",fg="white")
        b1_txt.place(x=800,y=580,width =220,height=40)


        #Exit Button
        Exit=Image.open("Images/exit.png")
        Exit=Exit.resize((220,220),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg_Exit=ImageTk.PhotoImage(Exit)

        b1=Button(bg_image,image=self.photoimg_Exit,cursor="hand2",command=self.isExit)
        b1.place(x=1100,y=380,width =220,height=220)

        b1_txt=Button(bg_image,text="Exit",command=self.isExit,cursor="hand2",font=("PT Serif",15,"bold"),bg="#040229",fg="white")
        b1_txt.place(x=1100,y=580,width =220,height=40)




    




#############################Function buttons ###################
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def open_img(self):
        os.startfile("data")


    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def isExit(self):
        self.isExit=tkinter.messagebox.askyesno("Face recognition system","Are you sure want to exit?")
        if self.isExit>0:
            self.root.destroy()
        else:
            return


if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()