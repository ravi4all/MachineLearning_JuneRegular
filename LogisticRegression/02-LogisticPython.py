import numpy as np
import csv
import random

def read_csv(filename):
    dataset = []    
    with open(filename,'r') as file:
        data = csv.reader(file)        
        for row in data:
            dataset.append(row)    
    return dataset

def str_to_float(dataset):
    for row in range(len(dataset)):
        for col in range(len(dataset[0])):
            dataset[row][col] = float(dataset[row][col])

def min_max(dataset):
    minmax = []
    
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        min_value = min(col_values)
        max_value = max(col_values)
        minmax.append([min_value, max_value])
        
    return minmax
        

def normalization():
    pass

def cross_validation():
    pass

def accuracy_metrics():
    pass

def predictions(row,coef):
    ypred = coef[0]
    for i in range(len(row) - 1):
        ypred += coef[i+1] * row[i]
    return 1 / (1 + np.exp(-ypred))

def evaluate_algorithm():
    pass

def sgd_logistic():
    pass

def logistic_regression():
    pass

filename = 'pima-indians-diabetes.data.csv'
dataset = read_csv(filename)
str_to_float(dataset)
minmax = min_max(dataset)




