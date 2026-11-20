import cv2
import numpy as np

image = cv2.imread('image3.png')

gaussian_kernel = cv2.getGaussianKernel(5, 1.5)
gaussian_kernel = np.outer(gaussian_kernel, gaussian_kernel)
gaussian = cv2.filter2D(image, -1, gaussian_kernel)

kernel = np.ones((5, 5), dtype=np.float32) / 25
averaging = cv2.filter2D(image, -1, kernel)

median = cv2.medianBlur(image, 5)

sharpening_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
], dtype=np.float32)
sharpened = cv2.filter2D(image, -1, sharpening_kernel)

print("IMAGE 3 - ORIGINAL")
cv2.imshow("IMAGE 3 - ORIGINAL", image)
print("IMAGE 3 - GAUSSIAN")
cv2.imshow("IMAGE 3 - GAUSSIAN", gaussian)
print("IMAGE 3 - AVERAGING")
cv2.imshow("IMAGE 3 - AVERAGING", averaging)
print("IMAGE 3 - MEDIAN")
cv2.imshow("IMAGE 3 - MEDIAN", median)
print("IMAGE 3 - SHARPENED")
cv2.imshow("IMAGE 3 - SHARPENED", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()