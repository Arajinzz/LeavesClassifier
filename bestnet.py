#Hadjerci Mohammed Allaeddine

import numpy as np
import pickle as pkl
import keras
import shutil
import os
from random import shuffle
from preprocessing import load_obj
from keras import optimizers
from keras.callbacks import TensorBoard
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Activation

#load data
train_data = np.load('dataset/train_data.npy')
np.random.shuffle(train_data)

X = np.array([i[1] for i in train_data])
y = np.array([i[0] for i in train_data])

'''
dic = load_obj('dataset/labels_one_hot.pkl')
for key in dic:
    if np.array_equal(dic[key], y[0]):
        print(key)
print(X[0], y[0])
exit(0)
'''

layer_number = [0, 1, 2, 3, 4]
layers_size = [16, 32, 64, 128]

for layer_size in layers_size:
    for layer_count in layer_number:
        model_name = 'models/100_leaves-layersize{}-layercount{}.h5'.format(layer_size, layer_count+1)
        tb = TensorBoard(log_dir='logs/'+model_name)

        model = Sequential()
        
        model.add(Dense(layer_size, input_shape=(192,), activation='relu'))

        for _ in range(0, layer_count):
            model.add(Dense(layer_size, activation='relu'))
        
        model.add(Dense(100, activation='softmax'))

        adam = optimizers.adam(lr=0.001)
        model.compile(loss='categorical_crossentropy', optimizer=adam,
                      metrics=['accuracy'])
        
        model.fit(X, y, epochs=30, verbose=2, validation_split=0.2, callbacks=[tb])
        
        model.save(model_name)


'''
model = Sequential()
model.add(Dense(32, input_shape=(192,), activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(100, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X, y , epochs=500, verbose=2, validation_split=0.2)

model.save('test.h5')
'''