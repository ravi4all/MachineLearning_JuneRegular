import math
import csv
import random

def test_split(index,value,dataset):
    left, right = list(), list()
    
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
        
    return left, right
    

def gini_index(class_values, groups):
    gini = 0.0
    
    for class_value in class_values:
        
        for group in groups:
            size = len(group)

            if size == 0:
                continue
            
            proportion = [row[-1] for row in group].count(class_value) / size
            gini += proportion * (1.0 - proportion)
    
    return gini

def get_split(dataset, n_features):
    
    class_values = list(set([row[-1] for row in dataset]))
    b_index, b_values, b_score, b_groups = len(dataset), len(dataset), len(dataset), None
    
    features = list()
    
    while len(features) < n_features:
        index = random.randrange(len(dataset[0]))
        if index not in features:
            features.append(index)
    # print(features)
    for index in features:
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(class_values, groups)
            
            if gini < b_score:
                b_index, b_values, b_score, b_groups = index, row[index], gini, groups
                
    return {'index':b_index, 'score':b_score,'value':b_values}
    

def split():
    pass

def to_terminate():
    pass

def bagging():
    pass

def subsample():
    pass

def build_tree():
    pass

def random_forest():
    pass

dataset = [
        [2.7810836,2.550537003,0],
    	[1.465489372,2.362125076,0],
    	[3.396561688,4.400293529,0],
    	[1.38807019,1.850220317,0],
    	[3.06407232,3.005305973,0],
    	[7.627531214,2.759262235,1],
    	[5.332441248,2.088626775,1],
    	[6.922596716,1.77106367,1],
    	[8.675418651,-0.242068655,1],
    	[7.673756466,3.508563011,1]
    ]
n_features = 1

# get_split(dataset, n_features)