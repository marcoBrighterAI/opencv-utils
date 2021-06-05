# USAGE
# python flip.py

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="assets/opencv_logo.png",
                help="path to the input image")
args = vars(ap.parse_args())

# load the original input image and display it to our screen
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# flip the image horizontally
print("[INFO] flipping image horizontally...")
flipped_horizontally = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped_horizontally)
cv2.waitKey(0)

# flip the image vertically
print("[INFO] flipping image vertically...")
flipped_vertically = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped_vertically)
cv2.waitKey(0)

# flip the image along both axes
print("[INFO] flipping image horizontally and vertically...")
flipped_horizontally_and_vertically = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped_horizontally_and_vertically)
cv2.waitKey(0)
