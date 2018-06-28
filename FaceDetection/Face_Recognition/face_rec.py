import numpy as np
import cv2

cam = cv2.VideoCapture(0)
face_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

font = cv2.FONT_HERSHEY_SIMPLEX

f_01 = np.load('face_1.npy').reshape((20, 50 * 50 * 3))  # face_1
f_02 = np.load('face_2.npy').reshape((20, 50 * 50 * 3))  # face_2

names = {
    0: 'vaibhav',
    1: 'akash',
}

labels = np.zeros((40, 1))
labels[:20, :] = 0.0  # first 20 for user_1 (0)
labels[20:, :] = 1.0  # next 20 for user_2 (1)

# combine all info into one data array
data = np.concatenate([f_01, f_02])  # (60, 7500)
print(data.shape, labels.shape)  # (60, 1)

def distance(x1, x2):
    return np.sqrt(((x1 - x2) ** 2).sum())

def knn(x, train, targets, k=5):
    m = train.shape[0]
    dist = []
    for ix in range(m):
        # compute distance from each point and store in dist
        dist.append(distance(x, train[ix]))
    dist = np.asarray(dist)
    indx = np.argsort(dist)
    print("Index...",indx)
    sorted_labels = labels[indx][:k]
    print("Sorted...",sorted_labels)
    counts = np.unique(sorted_labels, return_counts=True)
    print("Count...",counts)
    return counts[0][np.argmax(counts[1])]


while True:
    ret, frame = cam.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cas.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            face_component = frame[y:y + h, x:x + w, :]
            fc = cv2.resize(face_component, (50, 50))

            lab = knn(fc.flatten(), data, labels)
            text = names[int(lab)]
        cv2.putText(frame, text, (x, y), font, 1, (255, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow('face recognition', frame)
        k = cv2.waitKey(33) & 0xFF
        if k == 27:
            break
    else:
        print('Error')

cam.release()
cv2.destroyAllWindows()
