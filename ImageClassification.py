# all of our data is of the same dimensions
# we need to create our feature matrix and our label matrix
import keras
from keras.preprocessing.image import ImageDataGenerator
import keras
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import tensorflow as tf
from sklearn.model_selection import RepeatedKFold
import matplotlib.pyplot as plt

# apply some transformations to the data to somewhat differentiate it if we want
# train_datagen = ImageDataGenerator(rescale = 1./255,
#                                   shear_range = 0.2, #maybe not do this
#                                   zoom_range = 0.2, # maybe not do this
#                                   horizontal_flip = False)

# parameters for CNN								   
batch_size = 32
epochs = 5
num_classes = 2

# input image dimensions
img_width, img_height = 150, 150

num_train_samples = 2300
num_test_samples = 700

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)


# implement CNN
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# load in the image
# need separate directories for the images based on where the break is
datagen = ImageDataGenerator(rescale=1./255)
training_set = datagen.flow_from_directory('data/train', 
                target_size = (img_width, img_height), batch_size = batch_size,
                class_mode = 'binary')
test_set = datagen.flow_from_directory('data/test', 
                target_size = (img_width, img_height), batch_size = batch_size,
                class_mode = 'binary')

history = model.fit_generator(
    training_set,
    steps_per_epoch=num_train_samples // batch_size,
    epochs=epochs,
    validation_data=test_set,
    validation_steps=num_test_samples // batch_size)

# plot results
# summarize history for accuracy
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()