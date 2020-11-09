#import the necessary packages
from imutils import paths
import argparse
import imutils
import cv2
import os

#cái này kiểu như mình gắn nhãn cho từng thằng á trong tập dữ liệu kia kìa nó hiện số gì nhấn số đó =))) thằng óc bò

#construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required = True, help = "path to input directory of images")
ap.add_argument("-a", "--annot", required = True, help = "path to output directory of annotations")
args = vars(ap.parse_args())

#grab the image paths then initilize the directory of character counts
imagePaths = list(paths.list_images(args["input"]))
counts = {}

#loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
    #display an update to the user
    print("[INFO] processing image {}/{}".format(i + 1, len(imagePaths)))
    try:
        #load the image and convert it to grayscale, then pad the image to ensure digits caught on the border of the image are retained
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.copyMakeBorder(gray, 8, 8, 8, 8, cv2.BORDER_REPLICATE)
        #theshold the image to reveal the digits
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

        #find countours in the image, keeping only the four largest ones
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        # cnts = cnts[1] if imutils.is_cv2() else cnts[0]
        # print("1", cnts)
        cnts = sorted(cnts, key=lambda x: cv2.contourArea(x), reverse=True)[:4]

        #loop over the contours
        for c in cnts:
            #compute the bounding box for the contour then extract the digit
            (x, y, w, h) = cv2.boundingRect(c)
            roi = gray[y - 5:y + h + 5, x - 5:x + w +5]

            cv2.namedWindow("ROI", cv2.WINDOW_NORMAL)
            #display the character, making it large enough for us to see, then wait for a keypress
            cv2.imshow("ROI", imutils.resize(roi, width = 28))
            key = cv2.waitKey(0)
            if key == ord("`"):
                print("[INFO] ignoring character")
                continue

            #grab the key that was pressed and construct the path the output directory
            key = chr(key).upper()
            dirPath = os.path.sep.join([args["annot"], key])
            #if the output directory does not exist, create it
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)

            #Write the labeled character to file
            count = counts.get(key, 1)
            p = os.path.sep.join([dirPath, "{}.png".format(str(count).zfill(6))])
            cv2.imwrite(p, roi)

            #increment the count for the current key
            counts[key] = count + 1

    except KeyboardInterrupt:
        print("[INFO] manally leaving script")
        break

    #an unknown error has occured for this particular image
    except Exception as e:
        print("[INFO] skipping image due to", e)