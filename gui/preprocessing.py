#Hadjerci Mohammed Allaeddine

from collections import defaultdict
import numpy as np
import pickle as pkl
from random import randint, shuffle


def save_obj(filename, obj):
    with open(filename, 'wb') as f:
        pkl.dump(obj, f, pkl.HIGHEST_PROTOCOL)

def load_obj(filename):
    with open(filename, 'rb') as f:
        return pkl.load(f)

def one_hot(size, index):
    o = np.zeros(size)
    o[index] = 1
    return o

def createLabs(name):
    labs = []
    for i in range(1, 65):
        labs.append(name+str(i))
    
    return labs

def createHead(header, name):
    for info in createLabs(name):
        header.append(info)

    return header

def get_data(file):
    data = defaultdict(list)
    with open(file, 'r') as f:
        f = f.readlines()
        for row in f:
            row = row.replace('\n', '')
            row = row.split(',')
            data[row[0]].append(row[1:])

    return data

def genData(filename, data):
    with open(filename, 'w') as f:
        for row in data:
            row = ','.join(row)
            f.write(row+'\n')

def getAllDataAndLabels():
    #header
    header = ['name']
    header = createHead(header, 'margin')
    header = createHead(header, 'shape')
    header = createHead(header, 'texture')

    margin_data = get_data('dataset/data_Mar_64.txt')
    shape_data = get_data('dataset/data_Sha_64.txt')
    texture_data = get_data('dataset/data_Tex_64.txt')

    del margin_data['Acer Campestre'][-1]
    del shape_data['Acer Campestre'][-1]

    all_data = []
    all_data.append(header)

    labels = []

    for key in margin_data:
        feature1 = margin_data[key]
        feature2 = shape_data[key]
        feature3 = texture_data[key]
        for i in range(0, len(feature1)):
            all_data.append([key]+feature1[i]+feature2[i]+feature3[i])
        
        labels.append(key)

    genData('dataset/all_data.txt', all_data)

    #get labels from keys
    labels = set(labels)
    labels_one_hot = {}

    i = 0

    for label in labels:
        labels_one_hot[label] = one_hot(len(labels), i)
        i+=1
    
    save_obj('dataset/labels_one_hot.pkl', labels_one_hot)

def splitData(filename, labfile, testsize):
    data = get_data(filename)
    labels = load_obj(labfile)

    del data['name']
    
    train_data = []
    test_data = []

    for key in data:
        features = data[key]

        for _ in range(0, testsize):
            indx = randint(0, len(features)-1)
            feature = np.array(features[indx]).astype(float)
            test_data.append(np.array([labels[key], feature]))
            del features[indx]

        for feature in features:
            feature = np.array(feature).astype(float)
            train_data.append(np.array([labels[key], np.array(feature)]))
        
    test_data = np.array(test_data)
    train_data = np.array(train_data)

    np.save('dataset/train_data.npy', train_data)
    np.save('dataset/test_data.npy', test_data)
    

#getAllDataAndLabels()
#splitData('dataset/all_data.txt', 'dataset/labels_one_hot.pkl', 3)

#DONE