# USAGE
# python image_drawing.py

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="hamdan.png",
	help="path to the input image")
ap.add_argument("-o", "--output", type=str, default="drawnpic.png",
	help="path to the input image")
args = vars(ap.parse_args())

# load the input image from disk
image = cv2.imread(args["image"])

# load the input image from disk
image = cv2.imread(args["image"])
# draw a circle around my face
cv2.circle(image, (650, 850), 180, (0, 255, 0), 5)
#two filled in circles covering my eyes,
cv2.circle(image, (700, 810), 30, (0, 255, 255), -1)
cv2.circle(image, (595, 810), 30, (0, 255, 255), -1)
#a rectangle over top of my mouth
cv2.rectangle(image, (700, 950), (600, 900), (0, 0, 255), -1)


# show the output image
cv2.imshow("drawn pic", image)
# Saving the image
cv2.imwrite(args['output'], image)

cv2.waitKey(0)