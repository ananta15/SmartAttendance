from tkinter import *
from tkinter import ttk  #Containes style toolkit
from PIL import Image,ImageTk  # pil-pillow
from tkinter import messagebox
import mysql.connector
import csv
import cv2
import os

class Student:
    def __init__(self,root):
        self.root=root
        # geometry set
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        ##################################### Variables #####################################
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_std_email=StringVar()
        self.var_phone_no=StringVar()
        self.var_add=StringVar()
        self.var_cgpa=StringVar()
        self.var_mentor=StringVar()
        self.var_ForG=StringVar()




        img=Image.open("Images/students.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg=ImageTk.PhotoImage(img)

        first_lb=Label(self.root, image=self.photoimg)
        first_lb.place(x=0,y=0,width=500,height=130)


        # img1=Image.open("Images/face_recog_3.png")
        img1=Image.open("Images/facere.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg1=ImageTk.PhotoImage(img1)

        first_lb=Label(self.root, image=self.photoimg1)
        first_lb.place(x=500,y=0,width=500,height=130)


        img2=Image.open("Images/stdents2.jpg")
        img2=img2.resize((530,130),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_lb=Label(self.root, image=self.photoimg2)
        first_lb.place(x=1000,y=0,width=530,height=130)


        # img3=Image.open("Images/juet_logo_1.jpg")
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


        title_lb=Label(bg_image,text="STUDENT MANAGEMENT SYSTEM",font=("PT Serif",35,"bold"),bg="#163b06",fg="#e6f2e1")
        title_lb.place(x=0,y=0,width=1530,height=50)

        main_frame=Frame(bg_image,bd=2,bg="#f0ecdf")
        main_frame.place(x=10,y=55,width=1500,height=600)

        # left label frame

        left_frame=LabelFrame(main_frame,bd=2,bg="#f0ecdf",relief=RIDGE,text="Student Details",font=("time new roman",13,"bold"))
        left_frame.place(x=10,y=10,width=745,height=580)

        img_lf=Image.open("Images/attendance.jpg")
        img_lf=img_lf.resize((730,130),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg_lf=ImageTk.PhotoImage(img_lf)

        first_lb=Label(left_frame, image=self.photoimg_lf)
        first_lb.place(x=10,y=10,width=720,height=130)


  
        #current course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="#f0ecdf",relief=RIDGE,text="Current Course Information",font=("time new roman",13,"bold"))
        current_course_frame.place(x=10,y=135,width=720,height=115)
        
        
        # Department
        dep_label=Label(current_course_frame,text="Department:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("time new roman",12,"bold"),state="readonly",width=20)
        dep_combo['values']=("Select Department","CSE","Civil","Mechanical","ECE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        # Course
        course_label=Label(current_course_frame,text="Course:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("time new roman",12,"bold"),state="readonly",width=20)
        course_combo['values']=("Select Course","B.Tech","Bsc","M.Tech","Phd")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        # Year
        year_label=Label(current_course_frame,text="Year:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("time new roman",12,"bold"),state="readonly",width=20)
        year_combo['values']=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=10,sticky=W)

        # Semester
        sem_label=Label(current_course_frame,text="Semester:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("time new roman",12,"bold"),state="readonly",width=20)
        sem_combo['values']=("Select Semester","1st","2nd","3rd","4th","5th","6th")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=5,pady=10,sticky=W)

        # Class student Information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="#f0ecdf",relief=RIDGE,text="Student Information",font=("time new roman",13,"bold"))
        class_student_frame.place(x=10,y=250,width=720,height=305)
        
        # Student Id
        studentId_label=Label(class_student_frame,text="Student ID:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("time new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        # Student Name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=22,font=("time new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        # Student Email
        studentEmail_label=Label(class_student_frame,text="Student Email:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        studentEmail_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        studentEmail_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_email,width=20,font=("time new roman",12,"bold"))
        studentEmail_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Gender
        studentGender_label=Label(class_student_frame,text="Gender:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        studentGender_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentGender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,state="readonly",font=("time new roman",12,"bold"))
        studentGender_combo['values']=("Select Gender","Male","Female","Others")
        studentGender_combo.current(0)
        studentGender_combo.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Phone No
        PhoneNo_label=Label(class_student_frame,text="Phone No:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        PhoneNo_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        PhoneNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone_no,width=20,font=("time new roman",12,"bold"))
        PhoneNo_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        # Address
        address_label=Label(class_student_frame,text="Address:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        address_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_add,width=22,font=("time new roman",12,"bold"))
        address_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
       
       
        # Father/Gardian Name
        Father_Gardian_Name=Label(class_student_frame,text="Father/Gardian:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        Father_Gardian_Name.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Father_Gardian_Name=ttk.Entry(class_student_frame,textvariable=self.var_ForG,width=20,font=("time new roman",12,"bold"))
        Father_Gardian_Name.grid(row=3,column=1,padx=10,pady=5,sticky=W)
       
        # DOB
        DOB=Label(class_student_frame,text="DOB:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        DOB.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        DOB=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=22,font=("time new roman",12,"bold"))
        DOB.grid(row=3,column=3,padx=10,pady=5,sticky=W)
       
        # Eno
        Eno=Label(class_student_frame,text="E. NO.:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        Eno.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Eno=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("time new roman",12,"bold"))
        Eno.grid(row=4,column=1,padx=10,pady=5,sticky=W)
       
       
        # Mentor 
        Mentor=Label(class_student_frame,text="Mentor:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        Mentor.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        Mentor=ttk.Entry(class_student_frame,textvariable=self.var_mentor,width=22,font=("time new roman",12,"bold"))
        Mentor.grid(row=4,column=3,padx=10,pady=5,sticky=W)
       
        # cgpa
        CGPA=Label(class_student_frame,text="CGPA:",font=("time new roman",12,"bold"),bg="#f0ecdf")
        CGPA.grid(row=5,column=0,padx=10,pady=5,sticky=W)

        CGPA=ttk.Entry(class_student_frame,textvariable=self.var_cgpa,width=20,font=("time new roman",12,"bold"))
        CGPA.grid(row=5,column=1,padx=10,pady=5,sticky=W)

        #Radio Buttons
        self.var_radio1=StringVar()
        radio1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radio1.grid(row=5,column=2)
        
        radio2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radio2.grid(row=5,column=3)


        #  Button Frame
        btn_frame=LabelFrame(class_student_frame,bd=2,bg="#f0ecdf",relief=RIDGE)
        btn_frame.place(x=10,y=210,width=700,height=45)

        #Save btn
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("time new roman",12,"bold"),bg="grey",fg="white")
        save_btn.grid(row=0,column=0,padx=10,pady=5)

        #Update btn
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("time new roman",12,"bold"),bg="grey",fg="white")
        update_btn.grid(row=0,column=1,padx=5,pady=5)

        #Delete btn
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("time new roman",12,"bold"),bg="grey",fg="white")
        delete_btn.grid(row=0,column=2,padx=5,pady=5)

        #Reset btn
        Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("time new roman",12,"bold"),bg="grey",fg="white")
        Reset_btn.grid(row=0,column=3,padx=10,pady=5)

        # Second Button Frame
        btn_frame_2=LabelFrame(class_student_frame,bd=2,bg="#f0ecdf",relief=RIDGE)
        btn_frame_2.place(x=10,y=245,width=700,height=35)

        #take photo btn
        take_photo_btn=Button(btn_frame_2,text="Take Photo",command=self.generate_dataset,width=32,font=("time new roman",12,"bold"),bg="grey",fg="white")
        take_photo_btn.grid(row=0,column=0,padx=10)

        #Update photo btn
        # update_photo_btn=Button(btn_frame_2,text="Update Photo",width=32,font=("time new roman",12,"bold"),bg="grey",fg="white")
        # update_photo_btn.grid(row=0,column=1,padx=10)





        # Right label frame

        right_frame=LabelFrame(main_frame,bd=2,bg="#f0ecdf",relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        right_frame.place(x=765,y=10,width=725,height=580)

        img_rt=Image.open("Images/attendance2.jpg")
        img_rt=img_rt.resize((700,125),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg_rf=ImageTk.PhotoImage(img_rt)

        first_lb=Label(right_frame, image=self.photoimg_rf)
        first_lb.place(x=10,y=10,width=700,height=125)

        ############################### Search System ###############################
        
        search_frame=LabelFrame(right_frame,bd=2,bg="#f0ecdf",relief=RIDGE,text="Search System",font=("time new roman",13,"bold"))
        search_frame.place(x=5,y=135,width=705,height=70)

        Search=Label(search_frame,text="Search By:",font=("time new roman",15,"bold"),bg="#f0ecdf",fg="dark blue")
        Search.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("time new roman",12,"bold"),state="readonly",width=12)
        search_combo['values']=("Select","Roll_No","Phone_No","Student_ID","D.O.B","Student_Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=17,font=("time new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=3,sticky=W)

        search_btn=Button(search_frame,text="Search",width=10,font=("time new roman",12,"bold"),bg="grey",fg="white")
        search_btn.grid(row=0,column=3,padx=5)
        
        showAll_btn=Button(search_frame,text="Show All",width=10,font=("time new roman",12,"bold"),bg="grey",fg="white")
        showAll_btn.grid(row=0,column=4,padx=5)

        #Table Frame

        Table_frame=Frame(right_frame,bd=2,bg="#f0ecdf",relief=RIDGE)
        Table_frame.place(x=5,y=210,width=705,height=340)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(Table_frame,column=("dep","course","year","sem","Student_ID","Student_Name","Student_Email","Gender","Phone_no","Address","Name(F/G)","D.O.B","CGPA","Mentor","Photo","Enrollment_No"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("Student_ID",text="Student_ID")
        self.student_table.heading("Student_Name",text="Student_Name")
        self.student_table.heading("Student_Email",text="Student_Email")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Phone_no",text="Phone_no")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Name(F/G)",text="Name(Father/Guardian)")
        self.student_table.heading("D.O.B",text="D.O.B")
        self.student_table.heading("CGPA",text="CGPA")
        self.student_table.heading("Mentor",text="Mentor")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table.heading("Enrollment_No",text="Enrollment_No")
        
        self.student_table["show"]="headings"

    
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        
        self.student_table.column("Student_Name",width=100)
        self.student_table.column("Student_Email",width=100)
        self.student_table.column("Student_ID",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Phone_no",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Name(F/G)",width=150)
        self.student_table.column("D.O.B",width=100)
        self.student_table.column("CGPA",width=100)
        self.student_table.column("Mentor",width=100)
        self.student_table.column("Photo",width=150)
        self.student_table.column("Enrollment_No",width=100)
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    ######################################### Function declaration #########################################

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_std_email.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_ForG.get()=="" or self.var_add.get()=="" or self.var_phone_no.get()=="" or self.var_roll.get()=="" or self.var_mentor.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            #messagebox.showinfo("Success","Your Information Has Been Submitted")
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='abhi2021',database='face_recognition')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into student_detail values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_std_email.get(),
                    self.var_gender.get(),
                    self.var_phone_no.get(),
                    self.var_add.get(),
                    self.var_ForG.get(),
                    self.var_dob.get(),
                    self.var_cgpa.get(),
                    self.var_mentor.get(),                
                    self.var_radio1.get(),
                    self.var_roll.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added succcessfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)
            


    ######################################### Fetch data #########################################
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='abhi2021',database='face_recognition')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student_detail")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

######################################### get cursor #########################################

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        print(data)
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_std_email.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_phone_no.set(data[8]),
        self.var_add.set(data[9]),
        self.var_ForG.set(data[10]),
        self.var_dob.set(data[11]),
        self.var_cgpa.set(data[12]),
        self.var_mentor.set(data[13]),
        self.var_radio1.set(data[14]),
        self.var_roll.set(data[15])
        


######################################## updarte functiom #########################################
    
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_std_email.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_ForG.get()=="" or self.var_add.get()=="" or self.var_phone_no.get()=="" or self.var_cgpa.get()=="" or self.var_mentor.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update",parent=self.root)
                if(update>0):
                    conn=mysql.connector.connect(host='localhost',username='root',password='abhi2021',database='face_recognition')
                    my_cursor=conn.cursor()
                    sql="""UPDATE student_detail SET dep= %s,course= %s,year= %s,semester= %s,name= %s,email= %s,gender= %s,phone= %s, address= %s,guardian=%s, dob= %s,cgpa= %s,teacher=%s,photosample= %s,eno=%s where student_id= %s"""
                    val=(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_std_name.get(),
                        self.var_std_email.get(),
                        self.var_gender.get(),
                        self.var_phone_no.get(),
                        self.var_add.get(),
                        self.var_ForG.get(),
                        self.var_dob.get(),
                        self.var_cgpa.get(),
                        self.var_mentor.get(),                
                        self.var_radio1.get(),
                        self.var_roll.get(),

                        self.var_std_id.get()

                    )

                    my_cursor.execute(sql,val)
                else:
                    if not update:
                        return 

                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","student detail successfully updated",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)

            
            


    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete",parent=self.root)
                if(delete>0):
                    conn=mysql.connector.connect(host='localhost',username='root',password='abhi2021',database='face_recognition')
                    my_cursor=conn.cursor()
                    sql='delete from student_detail where student_id=%s'
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return 

                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","student detail successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    def reset_data(self):
        self.var_dep.set("Select department")
        self.var_course.set("Select course")
        self.var_year.set("Select year")
        self.var_sem.set("Select semester")
        self.var_std_name.set("")
        self.var_div.set("Select division")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_std_email.set("")
        self.var_phone_no.set("")
        self.var_add.set("")
        self.var_mentor.set("")
        self.var_radio1.set("")
        self.var_std_id.set("")
        self.var_ForG.set("")
        self.var_cgpa.set("")
        


####### generate dataset or take photos  #####
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_std_email.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_ForG.get()=="" or self.var_add.get()=="" or self.var_phone_no.get()=="" or self.var_cgpa.get()=="" or self.var_mentor.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='abhi2021',database='face_recognition')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student_detail")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1

                
                #conn=mysql.connector.connect(host='localhost',username='root',password='abhi2021',database='face_recognition')
                 #   my_cursor=conn.cursor()
                sql="""UPDATE student_detail SET dep= %s,course= %s,year= %s,semester= %s,name= %s,email= %s,gender= %s,phone= %s, address= %s,guardian=%s, dob= %s,cgpa= %s,teacher=%s,photosample= %s,eno=%s where student_id= %s"""
                val=(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_std_name.get(),
                        self.var_std_email.get(),
                        self.var_gender.get(),
                        self.var_phone_no.get(),
                        self.var_add.get(),
                        self.var_ForG.get(),
                        self.var_dob.get(),
                        self.var_cgpa.get(),
                        self.var_mentor.get(),                
                        self.var_radio1.get(),
                        self.var_roll.get(),

                        self.var_std_id.get()

                    )

                my_cursor.execute(sql,val)

                #my_cursor.execute(sql,val) 
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                 

                    
                # face detection start
                cam = cv2.VideoCapture(0)
                harcascadePath = "./Cascades/haarcascade_frontalface_default.xml"
                face_classifier = detector = cv2.CascadeClassifier(harcascadePath)
                sampleNum = 0

                while(True):
                    ret, img = cam.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30,30),flags = cv2.CASCADE_SCALE_IMAGE)
                    for(x,y,w,h) in faces:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (10, 159, 255), 2)
                        sampleNum = sampleNum+1
                        #saving the captured face in the dataset folder TrainingImage
                        cv2.imwrite("data/image." + str(id) + '.' +
                                    str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                        cv2.imshow('frame', img)
                    if cv2.waitKey(30) & 0xFF == ord('q'):
                        break
                    elif sampleNum > 30:
                        break
                cam.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set successfully")

            except Exception as es:
                print(es)
                #messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    




if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()