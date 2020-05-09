import keras
import numpy as np
import os
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, Conv3D
from sklearn.model_selection import train_test_split

WIDTH = 80
HEIGHT = 60
NUM_OF_CLASSES = 11
LR = 0.0001
EPOCHS = 25
BATCH_SIZE = 32

save_dir = os.path.join(os.getcwd(), 'saved_models')
model_name = 'new_model.h5'

np_load_old = np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
train_data = np.load('training_data/training_data_balanced.npy')
np.load = np_load_old

X = np.array([i[0] for i in train_data]).reshape(-1,WIDTH,HEIGHT,1)
y = np.array([i[1] for i in train_data])

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

model = Sequential()
model.add(Conv2D(32, (3, 3), padding='same', input_shape=x_train.shape[1:], activation='relu'))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(NUM_OF_CLASSES, activation='softmax'))

opt = keras.optimizers.RMSprop(learning_rate=LR, decay=1e-6)
model.compile(loss='categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

model.fit(x_train, y_train,
          batch_size=BATCH_SIZE,
          epochs=EPOCHS,
          validation_data=(x_test, y_test),
          shuffle=True)

if not os.path.isdir(save_dir):
    os.makedirs(save_dir)
model_path = os.path.join(save_dir, model_name)
model.save(model_path)
print('Saved trained model at %s ' % model_path)

scores = model.evaluate(x_test, y_test, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])