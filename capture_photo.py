import cv2
import os
import csv


def info(ID,NAME):

    ID = int(input("Enter student ID: "))
    NAME = input("Enter student name: ")

def capture(ID,NAME):

    with open('data.csv', 'a') as newFile:
        newFileWriter = csv.writer(newFile)
        newFileWriter.writerow([ID, NAME])

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