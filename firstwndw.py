from tkinter import *
import cv2
import os
import csv
import face_recon_module as fr
from datetime import date

employee_ID = []
employee_data = []

def create_salary_sheet():



    with open('data.csv', mode='r', newline="") as data:
        reader = csv.reader(data)
        for rows in reader:
            employee_ID.append(rows[0])
            employee_data.append(rows[0])



    for file in os.listdir("E:\\face_recon\\attendance\\"):
        with open("E:\\face_recon\\attendance\\"+ file, 'r', newline="") as attendance_sheet:
            reader = csv.reader(attendance_sheet)
            for rows in reader:
                if rows[0] in employee_ID:
                    for i in range(len(employee_ID)):
                        if employee_ID[i] == rows[0]:
                            employee_data[i] = int(employee_data[i]) + 1

    with open('Salary_sheet.csv', 'w', newline="") as sheet:
        writer = csv.writer(sheet)
        for i in range(len(employee_ID)):
            writer.writerow([employee_ID[i], str(int(employee_data[i]) - int(employee_ID[i])) + " P days"
                                , "<% cut according to firm>"])


def output():
    today = date.today()
    print("Today's date:", today)

    video = cv2.VideoCapture(0)

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read("E:\\face_recon\\trained_images\\trained_data.yml")

    name = {}

    with open('data.csv', mode='r') as infile:
        reader = csv.reader(infile)
        for rows in reader:
            if rows != []:
                ID = int(rows[0])
                NAME = rows[1]
                name[ID] = NAME

    while True:
        check, frame = video.read()
        faces_detected, gray_img = fr.facerecon(frame)

        for (x,y,w,h) in faces_detected:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), thickness=4)

        for face in faces_detected:
            (x,y,w,h) = face
            roi_gray = gray_img[y:y+w, x:x+h]
            label, confidence = face_recognizer.predict(roi_gray)
            print("confidence :", confidence)
            print("label :", label)
            fr.draw_rect(frame, face)
            predicted_name = name[label]
            if confidence < 50:
                fr.put_text(frame, predicted_name, x, y)

        resized_img = cv2.resize(frame, (720,480))
        cv2.imshow("face :", resized_img)
        key = cv2.waitKey(1)
        if key == ord('n'):
            continue

        #     Marking attendance ...
        if key == ord('y'):
            with open('E:\\face_recon\\attendance\\attendance'+ str(today) +'.csv', 'a', newline="") as newFile:
                newFileWriter = csv.writer(newFile)
                newFileWriter.writerow([label, name[label], "Present"])
            break
        if key == ord('q'):
            break

    video.release()


def sec():



    def train():

        faces, faceID = fr.data_for_training("E:\\face_recon\\sample_images\\")

        face_recognizer = fr.train_data(faces, faceID)
        face_recognizer.save("E:\\face_recon\\trained_images\\trained_data.yml")
        print(faces,faceID)


    def cap(ID,NAME):
        with open('data.csv', 'a') as newFile:
            newFileWriter = csv.writer(newFile)
            newFileWriter.writerow([ID, NAME])

    def info(ID,NAME):


        video = cv2.VideoCapture(0)
        count = 1

        os.mkdir("E:\\face_recon\\sample_images\\"+str(ID)+"\\")
        while True:
            count += 1
            check, frame = video.read()

            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow("capture", frame)

            key = cv2.waitKey(1)

            cv2.imwrite("E:\\face_recon\\sample_images\\"+str(ID)+"\\frame%d.jpg" % count, frame)

            if count == 100:
                break
            if key == ord('q'):
                break



        video.release()
        print(count)


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

    roll = IntVar()

    lbl_roll=Label(Manage_Frame,text="Roll no.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
    lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

    txt_Roll=Entry(Manage_Frame,textvariable=roll,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")


    NAME = StringVar()

    lbl_name=Label(Manage_Frame,text="Student Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
    lbl_name.grid(row=6,column=0,pady=80,padx=20,sticky="w")

    txt_name=Entry(Manage_Frame,textvariable=NAME,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
    txt_name.grid(row=6,column=1,pady=80,padx=20,sticky="w")


    Registbtn=Button(Manage_Frame,text="Register",width=10,bd=5,relief=GROOVE,font=("times new roman",13,"bold"),command =lambda: cap(txt_Roll.get(),txt_name.get()))
    Registbtn.place(x=150,y=450,width=200)

    #where we will add photo

    Training_Frame=Frame(top,bd=4,relief=RIDGE,bg="crimson")
    Training_Frame.place(x=500,y=100,width=800,height=560)

    photobtn=Button(Training_Frame,text="Add Photo",width=10,bd=5,relief=GROOVE,font=("times new roman",13,"bold"),command =lambda: info(txt_Roll.get(),txt_name.get()))
    photobtn.place(x=300,y=150,width=200,height=70)

    closebtn=Button(Training_Frame,text="X",width=10,bd=5,relief=GROOVE,font=("times new roman",13,"bold"),command=top.quit)
    closebtn.place(x=700,y=10,width=60)

    trainbtn=Button(Training_Frame,text="Train Model",width=10,bd=5,relief=GROOVE,font=("times new roman",13,"bold"),command = train)
    trainbtn.place(x=330,y=280,width=150)

    checkbtn=Button(Training_Frame,text="Give attendance",width=10,bd=5,relief=GROOVE,font=("times new roman",13,"bold"),command = output)
    checkbtn.place(x=330,y=380,width=150)

    backbtn=Button(Training_Frame,text="Go Back",width=10,bd=5,relief=GROOVE,font=("times new roman",13,"bold"),command = top.destroy)
    backbtn.place(x=330,y=480,width=150)


root=Tk()

root.title("Attendance")
root.geometry('500x500+480+180')

screen = Frame(root,bg="gold")
screen.place(x=1,y=5,width=500,height=560)

button=Button(screen,text = "NEW USER",bd=5,font=("times new roman",10,"bold"),fg="white",relief=GROOVE,bg="red",command=sec)
button.place(x=100,y=100,width=300,height=50)

button=Button(screen,text = "GIVE ATTENDANCE",bg="white",bd=5,relief=GROOVE,font=("times new roman",10,"bold"),command = output)
button.place(x=100,y=200,width=300,height = 50)

button=Button(screen,text = "Create Salary Sheet",bg="white",bd=5,relief=GROOVE,font=("times new roman",10,"bold"),command = create_salary_sheet)
button.place(x=100,y=300,width=300,height = 50)

mainloop()