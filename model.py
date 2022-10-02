import os
from keras.preprocessing import image
import matplotlib.pyplot as plt 
import numpy as np
from keras.utils.np_utils import to_categorical
import random,shutil
from keras.models import Sequential
from keras.layers import Dropout,Conv2D,Flatten,Dense, MaxPooling2D, BatchNormalization
from keras.models import load_model
import splitfolders


def generator(dir, gen=image.ImageDataGenerator(rescale=1./255), shuffle=True,batch_size=1,target_size=(24,24),class_mode='categorical' ):

    return gen.flow_from_directory(dir,batch_size=batch_size,shuffle=shuffle,color_mode='grayscale',class_mode=class_mode,target_size=target_size)

BS= 32
TS=(24,24)
train_batch= generator('dataset_new/train_data/train',shuffle=True,batch_size = BS,target_size=TS)
valid_batch= generator('dataset_new/train_data/val',shuffle=True,batch_size = BS,target_size=TS)
test_batch = generator('Dataset/test',shuffle = False, target_size=TS)
SPE= len(test_batch.classes)//BS
VS = len(valid_batch.classes)//BS
print(SPE,VS)


model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(24,24,1)),
    MaxPooling2D(pool_size=(1,1)),
    Conv2D(32,(3,3),activation='relu'),
    MaxPooling2D(pool_size=(1,1)),
#32 convolution filters used each of size 3x3
#again
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(1,1)),

#64 convolution filters used each of size 3x3
#choose the best features via pooling
    
#randomly turn neurons on and off to improve convergence
    Dropout(0.25),
#flatten since too many dimensions, we only want a classification output
    Flatten(),
#fully connected to get all relevant data
    Dense(128, activation='relu'),
#one more dropout for convergence' sake :) 
    Dropout(0.5),
#output a softmax to squash the matrix into output probabilities
    Dense(2, activation='softmax')
])

model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

model.fit_generator(train_batch, validation_data=valid_batch,epochs=50,steps_per_epoch=SPE ,validation_steps=VS)

# Epoch 30/30
# 30/30 [==============================] - 3s 95ms/step - loss: 0.0186 - accuracy: 0.9948 - val_loss: 0.1252 - val_accuracy: 0.9598
# Epoch 50/50
# 30/30 [==============================] - 3s 103ms/step - loss: 2.1422e-04 - accuracy: 1.0000 - val_loss: 0.2001 - val_accuracy: 0.9688
model.save('models/cnnCat2.h5', overwrite=True)

#history = model.fit(train_generator, epochs=50, validation_data=test_generator, shuffle=True, validation_steps=len(test_generator))
#model.predict(test_batch)

# accuracy = history.history['accuracy']
# val_accuracy = history.history['val_accuracy']
# loss = history.history['loss']
# val_loss = history.history['val_loss']
# epochs = range(len(accuracy))

# plt.plot(epochs, accuracy, "b", label="trainning accuracy")
# plt.plot(epochs, val_accuracy, "r", label="validation accuracy")
# plt.legend()
# plt.show()

# plt.plot(epochs, loss, "b", label="trainning loss")
# plt.plot(epochs, val_loss, "r", label="validation loss")
# plt.legend()
# plt.show()

#predict = model.predict('')