import cv2
import face_recon_module as fr

test_img = cv2.imread("E:\\face_recon\\nitin.jpg")
faces_detected, gray_img = fr.facerecon(test_img)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("E:\\face_recon\\trained_images\\trained_data.yml")

name = {0:"nitin", 1:"neha"}

for face in faces_detected:
    (x,y,w,h) = face
    roi_gray = gray_img[y:y+w, x:x+h]
    label, confidence = face_recognizer.predict(roi_gray)
    print("confidence :", confidence)
    print("label :", label)
    fr.draw_rect(test_img, face)
    predicted_name = name[label]
    if confidence<50:
        fr.put_text(test_img, predicted_name, x, y)

resized_img = cv2.resize(test_img, (720,480))
cv2.imshow("image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()