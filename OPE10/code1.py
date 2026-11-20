import cv2
import numpy as np

image = cv2.imread('image1.png')

# Gaussian Smoothing
gaussian_kernel = cv2.getGaussianKernel(5, 1.5)
gaussian_kernel = np.outer(gaussian_kernel, gaussian_kernel)
gaussian = cv2.filter2D(image, -1, gaussian_kernel)

# Averaging Filter
kernel = np.ones((5, 5), dtype=np.float32) / 25
averaging = cv2.filter2D(image, -1, kernel)

# Median Filter
median = cv2.medianBlur(image, 5)

# High-Pass Sharpening
sharpening_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
], dtype=np.float32)
sharpened = cv2.filter2D(image, -1, sharpening_kernel)

print("IMAGE 1 - ORIGINAL")
cv2.imshow("IMAGE 1 - ORIGINAL", image)
print("IMAGE 1 - GAUSSIAN")
cv2.imshow("IMAGE 1 - GAUSSIAN", gaussian)
print("IMAGE 1 - AVERAGING")
cv2.imshow("IMAGE 1 - AVERAGING", averaging)
print("IMAGE 1 - MEDIAN")
cv2.imshow("IMAGE 1 - MEDIAN", median)
print("IMAGE 1 - SHARPENED")
cv2.imshow("IMAGE 1 - SHARPENED", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
