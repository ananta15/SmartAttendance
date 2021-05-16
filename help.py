from tkinter import*
from tkinter import ttk  #Containes style toolkit
from PIL import Image,ImageTk  # pil-pillow
from tkinter import messagebox
import mysql.connector

class Help:
    def __init__(self,root):
        self.root=root
        # geometry set
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lb1=Label(self.root,text="HELP DESK",font=("time new roman",35,"bold"),bg="white",fg="dark blue")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open("Images/help.jpg")
        img_top=img_top.resize((1530,740),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        first_lb=Label(self.root, image=self.photoimg_top)
        first_lb.place(x=0,y=55,width=1530,height=740)

        help_lb=Label(first_lb,text="Email: 181b041@juetguna.in",font=("time new roman",15,"bold"),fg="white",bg="black")
        help_lb.place(x=600,y=125)

        help_lb2=Label(first_lb,text="Email: 181b032@juetguna.in",font=("time new roman",15,"bold"),fg="white",bg="black")
        help_lb2.place(x=600,y=165)

        help_lb3=Label(first_lb,text="Email: 181b021@juetguna.in",font=("time new roman",15,"bold"),fg="white",bg="black")
        help_lb3.place(x=600,y=205)















if __name__== "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()