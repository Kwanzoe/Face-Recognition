from tkinter import *
from tkinter import ttk
import capture_photo as cp

def addname():
    print("Hello")

def sec():
    top=Toplevel()
    top.geometry('1350x700+0+0')
    top.title("Student Registration")

    title=Label(top,text="Student Attendance System",bd=10,relief=GROOVE,font=("times new roman",30,"bold"),bg="green",fg="yellow")
    title.pack(side=TOP,fill=X)

    #LEFT...FRAME

    Manage_Frame=Frame(top,bd=4,relief=RIDGE,bg="crimson")
    Manage_Frame.place(x=20,y=100,width=450,height=560)

    m_title=Label(Manage_Frame,text="Manage Students",bg="crimson",fg="white",font=("times new roman",20,"bold"))
    m_title.grid(row=0,columnspan=2,pady=20)

    lbl_roll=Label(Manage_Frame,text="Roll no.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
    lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

    txt_Roll=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

    name = StringVar()

    lbl_name=Label(Manage_Frame,text="Student Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
    lbl_name.grid(row=6,column=0,pady=80,padx=20,sticky="w")

    txt_name=Entry(Manage_Frame,textvariable=name,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_name.grid(row=6,column=1,pady=80,padx=20,sticky="w")

    namebtn=Button(Manage_Frame,textvariable=name,width=8,bd=5,relief=GROOVE,font=("times new roman",13,"bold"))
    namebtn.place(x=270,y=270,width=100)

    lbl_branch=Label(Manage_Frame,text="Branch",bg="crimson",fg="white",font=("times new roman",20,"bold"))
    lbl_branch.grid(row=9,column=0,pady=10,padx=20,sticky="w")

    combo_branch=ttk.Combobox(Manage_Frame,font=("times new roman",13,"bold"),state='readonly')
    combo_branch['values']=("CSE","IT","ECE","BIOTECH")
    combo_branch.grid(row=9,column=1,padx=20,pady=10)


    Registbtn=Button(Manage_Frame,text="Register",width=10,bd=5,relief=GROOVE,font=("times new roman",13,"bold"))
    Registbtn.place(x=150,y=450,width=200)

    #where we will add photo

    Training_Frame=Frame(top,bd=4,relief=RIDGE,bg="crimson")
    Training_Frame.place(x=500,y=100,width=800,height=560)

    photobtn=Button(Training_Frame,text="Add Photo",width=10,bd=5,relief=GROOVE,font=("times new roman",13,"bold"),command=cp.capture)
    photobtn.place(x=300,y=150,width=200,height=70)

    closebtn=Button(Training_Frame,text="X",width=10,bd=5,relief=GROOVE,font=("times new roman",13,"bold"),command=top.quit)
    closebtn.place(x=700,y=10,width=60)


root=Tk()

button=Button(root,text = "NEW USER",bd=5,relief=GROOVE,command=sec)
button.place(x=150,y=100,width=200)

button=Button(root,text = "EXISTING USER",bd=5,relief=GROOVE)
button.place(x=150,y=200,width=200)



root.title("Attendance")
root.geometry('500x500+120+120')

mainloop()