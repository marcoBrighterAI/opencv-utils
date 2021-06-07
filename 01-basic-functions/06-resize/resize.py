# USAGE
# python resize.py

# import the necessary packages
import argparse
import cv2

from utils import resize

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="assets/lena.png",
                help="path to the input image")
args = vars(ap.parse_args())

# load the original input image and display it to our screen
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# let's resize our image to be 150 pixels wide, but in order to
# prevent our resized image from being skewed/distorted, we must
# first calculate the ratio of the *new* width to the *old* width
r = 250.0 / image.shape[1]
dim = (250, int(image.shape[0] * r))

# perform the actual resizing of the image
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)
cv2.waitKey(0)

# let's resize the image to have a width of 50 pixels, again keeping
# in mind the aspect ratio
r = 100.0 / image.shape[0]
dim = (int(image.shape[1] * r), 100)

# perform the resizing
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)

# construct the list of interpolation methods in OpenCV
methods = [
    ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
    ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
    ("cv2.INTER_AREA", cv2.INTER_AREA),
    ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
    ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]

# loop over the interpolation methods
for (name, method) in methods:
    # increase the size of the image by 3x using the current
    # interpolation method
    print("[INFO] {}".format(name))
    resized = resize(image, width=image.shape[1] * 3,
                     inter=method)
    cv2.imshow("Method: {}".format(name), resized)
    cv2.waitKey(0)
