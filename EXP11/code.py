import cv2
import numpy as np
import cv2
# Load the image
image = cv2.imread(r'C:\Users\Vrushank\OneDrive\Desktop\SEM 5\DSIP\EXP_11\o.jpg', 0)  # Load as grayscale

# Define the kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Perform Erosion
erosion = cv2.erode(image, kernel, iterations=1)

# Perform Dilation
dilation = cv2.dilate(image, kernel, iterations=1)

# Perform Opening (Erosion followed by Dilation)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Perform Closing (Dilation followed by Erosion)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Display the original image and the results
cv2.imshow('Original', image)
cv2.imshow('Erosion', erosion)
cv2.imshow('Dilation', dilation)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
