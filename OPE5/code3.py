import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('1.png', 0)

if img1 is None:
    raise ValueError("Image not found! Please check the image path.")

sizes = [3, 5, 7]

plt.figure(figsize=(12, 12))

for i, k in enumerate(sizes):
    kernel = np.ones((k, k), np.uint8)
    opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernel)

    plt.subplot(3, 3, i * 3 + 1)
    plt.imshow(img1, cmap='gray')
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(3, 3, i * 3 + 2)
    plt.imshow(opening, cmap='gray')
    plt.title(f"Opening {k}x{k}")
    plt.axis('off')

    plt.subplot(3, 3, i * 3 + 3)
    plt.imshow(closing, cmap='gray')
    plt.title(f"Closing {k}x{k}")
    plt.axis('off')

plt.tight_layout()
plt.show()