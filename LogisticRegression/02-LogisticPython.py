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

def normalization(minmax,dataset):
    numer = 0
    denom = 0
    
    for row in dataset:
        for col in range(len(row)):
            numer = row[col] - minmax[col][0]
            denom = minmax[col][1] - minmax[col][0]
            row[col] = numer / denom


def cross_validation(dataset, n_folds):
    dataset_copy = dataset.copy()
    fold_size = int(len(dataset) / n_folds)
    folds = []
    
    for i in range(n_folds):
        fold = []
        while len(fold) <= fold_size:
            index = random.randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
            
        folds.append(fold)
    return folds

def accuracy_metrics(actual,predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    
    return correct / len(actual) * 100

def predictions(row,coef):
    ypred = coef[0]
    for i in range(len(row) - 1):
        ypred += coef[i+1] * row[i]
    return 1 / (1 + np.exp(-ypred))

def evaluate_algorithm():
    pass

def sgd_logistic(dataset, learning_rate, nb_epochs):
    b = [0] * len(dataset[0])
    
    for i in range(nb_epochs):
        for row in dataset:
            yhat = predictions(row, b)
            error = row[-1] - yhat
            b[0] = b[0] + learning_rate * error * yhat * (1 - yhat)
            
            for j in range(len(row)):
                b[j+1] = b[j+1] + learning_rate * error * yhat * (1 - yhat) * row[j]
        

def logistic_regression():
    pass

filename = 'pima-indians-diabetes.data.csv'
dataset = read_csv(filename)
str_to_float(dataset)
minmax = min_max(dataset)
normalization(minmax, dataset)




