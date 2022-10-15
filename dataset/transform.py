#Hadjerci Mohammed Allaeddine
#Script pour generer test_with_labels et test_without_labels
from collections import defaultdict
import numpy as np
import pickle as pkl
from random import randint, shuffle

def load_obj(filename):
    with open(filename, 'rb') as f:
        return pkl.load(f)

test_data = np.load('test_data.npy')

X = np.array([i[1] for i in test_data])
y = np.array([i[0] for i in test_data])

labels = load_obj('labels_one_hot.pkl')

f1 = open('test_without_labels.txt', 'w')
f2 = open('test_with_labels.txt', 'w')

for feature, label in zip(X,y):
    feature = list(feature)
    f1.write(','.join(str(e) for e in feature)+'\n')

    for key in labels:
        if np.array_equal(labels[key], label):
            f2.write(key+','+','.join(str(e) for e in feature)+'\n')

f1.close()
f2.close()