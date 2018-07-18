import math
import csv
import random

def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = csv.reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset
 
def str_to_float(dataset):
    for row in dataset:
        for col in range(len(row)):
            row[col] = float(row[col])
 

def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for i in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = random.randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split

 
# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0
 
# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
	folds = cross_validation_split(dataset, n_folds)
	scores = list()
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
        #add each row in a given subsample to the test set
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		predicted = algorithm(train_set, test_set, *args)
#        print(predicted)
		actual = [row[-1] for row in fold]
		accuracy = accuracy_metric(actual, predicted)
		scores.append(accuracy)
	return scores

def predict():
    pass

# A split is comprised of an attribute in the dataset 
# and a value.
# We can summarize this as the index of an attribute to
# split and the value by which to split rows on that 
# attribute. This is just a useful shorthand for indexing
# into rows of data.

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
            
            proportion = [row[-1] for row in group].count(class_value) / size
            gini += proportion * (1.0 - proportion)
    
    return gini

def get_split(dataset, n_features):
    
    class_values = list(set([row[-1] for row in dataset]))
    b_index, b_values, b_score, b_groups = len(dataset), len(dataset), len(dataset), None
    
    features = list()
    
    while len(features) < n_features:
        index = random.randrange(len(dataset))
        if index not in features:
            features.append(index)
    
    for index in features:
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(class_values, groups)
            
            if gini < b_score:
                b_index, b_values, b_score, b_groups = index, row[index], gini, groups
                
    return {'index':b_index, 'score':b_score,'value':b_values}
    

def split(node,max_depth,min_features,depth):
    
    left, right = node['groups']
    del[node['groups']]
    
    if not left or not right:
        node['left'] = node['right'] = to_terminate(left + right)
        
    if len(left) >= max_depth or len(right) >= max_depth:
        node['left'], node['right'] = to_terminate(left), to_terminate(right)

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


# filename = 'german_credit.csv'
# dataset = load_csv(filename)
# str_to_float(dataset)

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