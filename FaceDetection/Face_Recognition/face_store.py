import cv2
import numpy as np

dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

data = []

while True:
    ret, img = cap.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = dataset.detectMultiScale(gray)
        # print(img)
        for x,y,w,h in face:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)
            face_comp = img[y:y+h, x:x+w, :]

            fc = cv2.resize(face_comp, (50,50))

            if len(data) < 20:
                data.append(fc)
            #print(data)

        if cv2.waitKey(2) == 27 or len(data) >= 20:
            break
        cv2.imshow('result',img)
    else:
        print("Some error")

data = np.asarray(data)
np.save('user_1.npy',data)

cv2.destroyAllWindows()
cap.release()
