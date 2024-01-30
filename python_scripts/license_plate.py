import cv2
import numpy as np

# Read the input image
image = cv2.imread('images.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur the image to reduce high frequency noise
gray = cv2.medianBlur(gray, 5)

# Apply adaptive thresholding to highlight the license plate
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Find contours in the thresholded image
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Find the contour with the largest area and assume it is the license plate
largest_area = 0
largest_contour_index = -1
for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if area > largest_area:
        largest_area = area
        largest_contour_index = i

# Extract the license plate region
if largest_contour_index >= 0:
    x,y,w,h = cv2.boundingRect(contours[largest_contour_index])
    license_plate = image[y:y+h, x:x+w]

# Save the license plate region to a new image file
cv2.imwrite('license_plate.jpg', license_plate)