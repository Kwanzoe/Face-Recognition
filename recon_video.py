import cv2
import face_recon_module as fr
import csv
from datetime import date

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
        if confidence<50:
            fr.put_text(frame, predicted_name, x, y)

    resized_img = cv2.resize(frame, (720,480))
    cv2.imshow("face :", resized_img)
    key = cv2.waitKey(1)
    if key == ord('n'):
        continue
    if key == ord('y'):
        with open('E:\\face_recon\\attendance\\attendance'+ str(today) +'.csv', 'a') as newFile:
            newFileWriter = csv.writer(newFile)
            newFileWriter.writerow([label, name[label]])
        break

video.release()
