from tkinter import *
from tkinter import ttk

class Student():
    def new(self,root1):

        title=Label(root1,text="Student Attendance System",bd=10,relief=GROOVE,font=("times new roman",30,"bold"),bg="green",fg="yellow")
        title.pack(side=TOP,fill=X)

        #LEFT...FRAME

        Manage_Frame=Frame(root1,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=560)

        m_title=Label(Manage_Frame,text="Manage Students",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_Frame,text="Roll no.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_Frame,text="Student Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=6,column=0,pady=80,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=6,column=1,pady=80,padx=20,sticky="w")

        lbl_branch=Label(Manage_Frame,text="Branch",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_branch.grid(row=9,column=0,pady=10,padx=20,sticky="w")

        combo_branch=ttk.Combobox(Manage_Frame,font=("times new roman",13,"bold"),state='readonly')
        combo_branch['values']=("CSE","IT","ECE","BIOTECH")
        combo_branch.grid(row=9,column=1,padx=20,pady=10)


        #where we will add photo

        Training_Frame=Frame(root1,bd=4,relief=RIDGE,bg="crimson")
        Training_Frame.place(x=500,y=100,width=800,height=560)

        photobtn=Button(Training_Frame,text="Add Photo",width=10,bd=5,relief=GROOVE,font=("times new roman",13,"bold"))
        photobtn.place(x=300,y=150,width=200,height=70)

