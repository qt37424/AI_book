import numpy as np
import cv2
import tensorflow.keras

imagePaths = cv2.imread('test_photo.jpg')

image = cv2.resize(imagePaths,(32, 32),interpolation=cv2.INTER_AREA)

test = np.array(image)

test = test.astype("float32")/255.0

print (test)

model = tensorflow.keras.models.load_model('final_model.h5')
prediction = model.predict(test)

print(prediction)
