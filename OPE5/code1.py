import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read Images
img1 = cv2.imread('1.png', 0)
img2 = cv2.imread('2.png', 0)
img3 = cv2.imread('3.png', 0)
img4 = cv2.imread('4.png', 0)

images = [img1, img2, img3, img4]
names = ["Image 1", "Image 2", "Image 3", "Image 4"]

# Check Images
for img in images:
    if img is None:
        raise ValueError("Image not found! Please check the image paths.")

# Apply Median Filters
plt.figure(figsize=(14, 12))

for i in range(4):
    median3 = cv2.medianBlur(images[i], 3)
    median5 = cv2.medianBlur(images[i], 5)
    median7 = cv2.medianBlur(images[i], 7)

    results = [
        images[i],
        median3,
        median5,
        median7
    ]

    titles = [
        names[i],
        "Median 3x3",
        "Median 5x5",
        "Median 7x7"
    ]

    for j in range(4):
        plt.subplot(4, 4, i * 4 + j + 1)
        plt.imshow(results[j], cmap='gray')
        plt.title(titles[j])
        plt.axis('off')

plt.tight_layout()
plt.show()

# Morphological Filtering on Image 1
kernel = np.ones((3, 3), np.uint8)

opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernel)

# Display Morphological Results
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(img1, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(opening, cmap='gray')
plt.title("Morphological Opening")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(closing, cmap='gray')
plt.title("Morphological Closing")
plt.axis('off')

plt.tight_layout()
plt.show()
