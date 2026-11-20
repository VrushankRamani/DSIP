
import cv2
import numpy as np

# Load the grayscale image
image = cv2.imread(
    r'C:\Users\Vrushank\OneDrive\Desktop\SEM 5\DSIP\EXP_11\o.jpg',
    cv2.IMREAD_GRAYSCALE
)

# Check whether image is loaded successfully
if image is None:
    print("Error: Image not found. Check the image path.")
    exit()

# Convert grayscale image into binary image using Otsu thresholding
_, binary = cv2.threshold(
    image, 0, 1, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# Define the structuring element
pattern = np.array([
    [ 0,  1,  0],
    [ 1,  1,  1],
    [ 0, -1,  0]
], dtype=np.int8)

# Apply Hit-or-Miss Transformation
result = cv2.morphologyEx(
    binary, cv2.MORPH_HITMISS, pattern
)

# Display Original Grayscale Image
print("Original Grayscale Image:")
cv2.imshow("Original Grayscale Image", image)

# Display Binary Image
print("Binary Image:")
cv2.imshow("Binary Image", binary * 255)

# Display Hit-or-Miss Result
print("Hit-or-Miss Result:")
cv2.imshow("Hit-or-Miss Result", result * 255)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
