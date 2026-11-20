import cv2
import matplotlib.pyplot as plt

images = [cv2.imread(f'{i}.png', 0) for i in range(1, 5)]

for img in images:
    if img is None:
        raise ValueError("Image not found! Please check the image paths.")

sizes = [3, 5, 9, 11]

plt.figure(figsize=(14, 12))

for i, img in enumerate(images):
    for j, k in enumerate(sizes):
        filtered = cv2.medianBlur(img, k)
        plt.subplot(4, 4, i * 4 + j + 1)
        plt.imshow(filtered, cmap='gray')
        plt.title(f"Image {i + 1} Median {k}")
        plt.axis('off')

plt.tight_layout()
plt.show()