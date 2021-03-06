from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from utils.captchahelper import preprocess
from imutils import contours
import numpy as np
import cv2

cv2.namedWindow('Output', cv2.WINDOW_NORMAL)

model = load_model("output/lenet.hdf5")
image = cv2.imread("test/5.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.copyMakeBorder(gray, 20, 20, 20, 20, cv2.BORDER_REPLICATE)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
cnts = sorted(cnts, key=lambda x: cv2.contourArea(x), reverse=True)[:4]
cnts = contours.sort_contours(cnts)[0]

caicanlam = cnts[0]

output = cv2.merge([gray]*3)

print(type(caicanlam))

for c in cnts:
    # compute the bounding box for the contour then extract the digit
    (x, y, w, h) = cv2.boundingRect(c)
    roi = gray[y - 5:y + h + 5, x - 5:x + w + 5]

    # pre-process the ROI and then classify it
    roi = preprocess(roi, 28, 28)
    roi = np.expand_dims(img_to_array(roi), axis=0) / 255.0
    pred = model.predict(roi).argmax(axis=1)[0] + 1

    # draw the prediction on the output image
    cv2.rectangle(output, (x - 2, y - 2), (x + w + 4, y + h + 4), (0, 255, 0), 1)
    cv2.putText(output, str(pred), (x - 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)

    # show the output
    cv2.imshow("Output", output)
    cv2.waitKey()
