import tensorflow.keras
# from PIL import Image, ImageOps
import cv2
import numpy as np

# Disable scientific notation for clarity
# np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('model/model.h5')

# # Create the array of the right shape to feed into the keras model
# # The 'length' or number of images you can put into the array is
# # determined by the first position in the shape tuple, in this case 1.
# data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# # Replace this with the path to your image
# image = Image.open('test.jpg')

# #resize the image to a 224x224 with the same strategy as in TM2:
# #resizing the image to be at least 224x224 and then cropping from the center
# size = (224, 224)
# image = ImageOps.fit(image, size, Image.ANTIALIAS)

# #turn the image into a numpy array
# image_array = np.asarray(image)

# # display the resized image
# image.show()

# # Normalize the image
# normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

# # Load the image into the array
# data[0] = normalized_image_array

id_to_label = {0: 'banana', 1: 'orange', 2: 'star_fruit'}

origin = cv2.imread('test_photo.jpg')

check = cv2.resize(origin, (64, 64))
check = cv2.cvtColor(check, cv2.COLOR_BGR2RGB)
check = np.array(check)
check = check[np.newaxis, :, :, :]
# check = check/255.0
# print(check)
# check = check.reshape(-1, 64, 64)
prediction = model.predict(check)

# run the inference
prediction = model.predict(check)
print(prediction)
print(np.argmax(prediction))
print("{}".format(id_to_label[np.argmax(prediction)]))
cv2.imshow("{}".format(id_to_label[np.argmax(prediction)]), origin)
cv2.waitKey()