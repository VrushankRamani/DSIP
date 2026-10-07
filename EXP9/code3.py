import cv2
import numpy as np

# Load the image
image = cv2.imread(r'C:\Users\Vrushank\OneDrive\Desktop\SEM 5\DSIP\EXP_9\p1.jpg')
# Define the size of the median filter kernel (should be an odd number)
kernel_size = 5
# You can adjust the size based on the desired smoothing level
# Apply the Median filter for smoothing
smoothed_image = cv2.medianBlur(image, kernel_size)
# Display the original and smoothed images
cv2.imshow('Original Image', image)
cv2.imshow('Smoothed Image', smoothed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()