from tkinter import*
from tkinter import ttk  #Containes style toolkit
from PIL import Image,ImageTk  # pil-pillow
from tkinter import messagebox
import mysql.connector

class Developer:
    def __init__(self,root):
        self.root=root
        # geometry set
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lb1=Label(self.root,text="DEVELOPER",font=("time new roman",35,"bold"),bg="white",fg="dark blue")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open("Images/dev.jpg")
        img_top=img_top.resize((1530,740),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        first_lb=Label(self.root, image=self.photoimg_top)
        first_lb.place(x=0,y=55,width=1530,height=740)


        # Frame
        main_frame=Frame(first_lb,bd=2,bg="white")
        main_frame.place(x=1000,y=55,width=500,height=625)

        img_l=Image.open("Images/developergif.gif")
        img_l=img_l.resize((200,200),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg_l=ImageTk.PhotoImage(img_l)

        first_lb=Label(main_frame, image=self.photoimg_l)
        first_lb.place(x=300,y=0,width=200,height=200)

        # Developer Info
        dev_lb=Label(main_frame,text="Akshat Mishra(181B021)",font=("time new roman",15,"bold"),bg="white",fg="#142552")
        dev_lb.place(x=10,y=45)

        dev_lb=Label(main_frame,text="Ananta Pandey(181B032)",font=("time new roman",15,"bold"),bg="white",fg="#142552")
        dev_lb.place(x=10,y=95)

        dev_lb=Label(main_frame,text="Anshika Gupta(181B041)",font=("time new roman",15,"bold"),bg="white",fg="#142552")
        dev_lb.place(x=10,y=145)

      






















if __name__== "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()