import cv2
import  os
import numpy as np

def facerecon(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_haar_cascade = cv2.CascadeClassifier("E:\\face_recon\\requirements\\haarcascade_frontalface_default.xml")
    faces = face_haar_cascade.detectMultiScale(gray_img, scaleFactor=1.32, minNeighbors=4)

    return faces, gray_img


def data_for_training(directory):
    faces = []
    faceID = []

    for path, subdirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith("."):
                print("skipping...")
                continue
            id = os.path.basename(path)
            img_path = os.path.join(path, filename)

            image=cv2.imread(img_path)
            if image is None:
                print("image not loaded properly")
                continue

            faces_rect, gray_img = facerecon(image)
            if len(faces_rect)!=1:
                continue

            (x,y,w,h) = faces_rect[0]
            roi_gray = gray_img[y:y+w, x:x+h]
            faces.append(roi_gray)
            faceID.append(int(id))
    return faces, faceID

def train_data(faces, faceID):
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces, np.array(faceID))
    return face_recognizer

def draw_rect(image, face):
    (x,y,w,h) = face
    cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), thickness=5)

def put_text(image, text, x, y):
    cv2.putText(image, text, (x,y), cv2.FONT_HERSHEY_DUPLEX, 2, (0,255,0), 6)
