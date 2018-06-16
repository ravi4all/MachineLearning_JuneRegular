import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

dataset = pd.read_csv('data/student.csv')

X = dataset['Math'].values
y = dataset['Reading'].values
z = dataset['Writing'].values

figure = plt.figure(figsize=(12,6))
ax = Axes3D(figure)
ax.scatter(X,y,z)
plt.show()

