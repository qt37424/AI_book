import imutils
import cv2

def preprocess(image, width, height):
    #grab the dimensions of the image, then initialize the padding values
    (h, w) = image.shape[:2]

    #if the width is greater than the height then resize along the width
    if w > h:
        image = imutils.resize(image, width = width)

    #otherwise, the height is greater than the width so resize along the heights
    else:
        image = imutils.resize(image, height = height)

    padW = int((width - image.shape[1]) / 2.0)
    padH = int((height - image.shape[0]) / 2.0)

    image = cv2.copyMakeBorder(image, padH, padH, padW, padW, cv2.BORDER_REPLICATE)
    image = cv2.resize(image, (width, height))
    #return the pre-processed image
    return image