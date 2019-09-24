#model
import tensorflow as tf
from tensorflow import keras
from keras import models
from keras.layers import Conv2D, Reshape
from keras.layers import Dense, Activation, Flatten, BatchNormalization, Dropout,MaxPooling2D
from keras.models import Sequential
from keras.layers import Layer, ZeroPadding2D, UpSampling2D
from keras.optimizers import Adam
from matplotlib.image import imread
from skimage.transform import resize 
import numpy as np


#prediction
def generate_prediction(img):
	#print ("no")
	
	model = models.Sequential()
	
	model.add(Conv2D(32, 3, activation='relu', padding='same', input_shape=(350, 350, 3)))
	model.add(BatchNormalization())
	model.add(Conv2D(32, 3, activation='relu', padding='same'))
	model.add(MaxPooling2D(2))
	model.add(Conv2D(64, 3, activation='relu', padding='same'))
	model.add(BatchNormalization())
	model.add(Conv2D(64, 3, activation='relu', padding='same'))
	model.add(MaxPooling2D(2))
	model.add(Conv2D(128, 3, activation='relu', padding='same'))
	model.add(BatchNormalization())
	model.add(Conv2D(128, 3, activation='relu', padding='same'))
	model.add(MaxPooling2D(2))
	model.add(Conv2D(256, 3, activation='relu', padding='same'))
	model.add(BatchNormalization())
	model.add(Conv2D(256, 3, activation='relu', padding='same'))
	model.add(MaxPooling2D(2))
	model.add(Flatten())
	model.add(Dense(256, activation='relu'))
	model.add(Dropout(0.1))
	model.add(Dense(128, activation='relu'))
	model.add(Dropout(0.1))
	model.add(Dense(64, activation='relu'))
	model.add(Dropout(0.1))
	model.add(Dense(32, activation='relu'))
	model.add(Dropout(0.1))
	model.add(Dense(6, activation='softmax'))

	model.compile(optimizer=Adam(lr=0.0001), 
				  loss='categorical_crossentropy', 
				  metrics=['accuracy'])

	
	
	model.load_weights('C:/Users/yalex/FlaskApp/attractiveness.hdf5') 
	img = img/255
	y = model.predict(img.reshape(1,350,350,3)) 
	model = None 
	return np.argmax(y)



#imgs = ['Images/AF1802.jpg', 'Images/AM247.jpg', 'Images/AM1161.jpg', 'Images/AF893.jpg', 'Images/AM1028.jpg']

