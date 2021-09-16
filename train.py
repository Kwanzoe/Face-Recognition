import face_recon_module as fr
import os

faces, faceID = fr.data_for_training("E:\\face_recon\\sample_images\\")

face_recognizer = fr.train_data(faces, faceID)
face_recognizer.save("E:\\face_recon\\trained_images\\trained_data.yml")
print(faces,faceID)
