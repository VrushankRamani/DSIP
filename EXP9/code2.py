import cv2
import numpy as np

# Load the image
image = cv2.imread(r'C:\Users\Vrushank\OneDrive\Desktop\SEM 5\DSIP\EXP_9\p1.jpg')
# Define the size of the Averaging filter kernel
kernel_size = (5, 5) 
# You can adjust the size based on the desired smoothing level
# Create the Averaging filter kernel
kernel = np.ones(kernel_size, dtype=np.float32) / (kernel_size[0] *
kernel_size[1])
# Apply the Averaging filter for smoothing
smoothed_image = cv2.filter2D(image, -1, kernel)
# Display the original and smoothed images
cv2.imshow('Original Image', image)
cv2.imshow('Smoothed Image', smoothed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()