import cv2
import numpy as np

face_1 = np.load('user_1.npy').reshape(20*50*50,3)
face_2 = np.load('user_2.npy').reshape(20*50*50,3)

def distance(x1,x2):
    return np.sqrt(sum(x2 - x1)**2)

def knn():
    pass