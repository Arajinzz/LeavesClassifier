#Hadjerci Mohammed Allaeddine

import numpy as np
import keras
from random import shuffle
from preprocessing import load_obj
from keras import optimizers
from keras.models import Sequential
from keras.layers import Dense, Dropout

#load data
train_data = np.load('dataset/train_data.npy')
np.random.shuffle(train_data)

X = np.array([i[1] for i in train_data])
y = np.array([i[0] for i in train_data])

model_name = '100_leaves-layersize{}-layercount{}.h5'.format(128, 2)
#tb = TensorBoard(log_dir='netlog/'+model_name)
model = Sequential()
        
model.add(Dense(128, input_shape=(192,), activation='relu'))
model.add(Dropout(0.4))

model.add(Dense(128, activation='relu'))
model.add(Dropout(0.4))

model.add(Dense(100, activation='softmax'))

adam = optimizers.adam(lr=0.001)
model.compile(loss='categorical_crossentropy', optimizer=adam,
                metrics=['accuracy'])

model.fit(X, y, epochs=500, verbose=2, validation_split=0.2)

model.save(model_name)
