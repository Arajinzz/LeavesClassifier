#Hadjerci Mohammed Allaeddine

import numpy as np
from preprocessing import one_hot, load_obj
from keras.models import load_model

#load data
test_data = np.load('dataset/test_data.npy')

dic = load_obj('dataset/labels_one_hot.pkl')

X = np.array([i[1] for i in test_data])
y = np.array([i[0] for i in test_data])

model = load_model('100_leaves-layersize128-layercount2.h5')
total = 0
totaltrue = 0

print('Wrong Classification')

for feature, label in zip(X, y):
    prediction = model.predict(feature.reshape(-1, 192))
    choice = np.argmax(prediction[0])

    if np.array_equal(one_hot(100, choice), label):
        totaltrue += 1
    else:
        newlab = ''
        for lab in dic:
            if np.array_equal(dic[lab], label):
                newlab = lab

        for lab in dic:
            if np.array_equal(one_hot(100, choice), dic[lab]):
                print('Classification : ' ,lab,', True Label : ',newlab)
    
    total += 1

print('Accuracy : ', totaltrue/total)