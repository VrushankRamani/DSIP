import cv2
import numpy as np 
import cv2_imshow  
image = cv2.imread('/Screenshot 2026-09-09 095140.png')  
# Gaussian Smoothing  gaussian_kernel = cv2.getGaussianKernel(5, 1.5)  gaussian_kernel = np.outer(gaussian_kernel, gaussian_kernel)  gaussian = cv2.filter2D(image, -1, gaussian_kernel)  
# Averaging Filter  kernel = np.ones((5, 5), dtype=np.float32) / 25  averaging = cv2.filter2D(image, -1, kernel)  
# Median Filter  median = cv2.medianBlur(image, 5)  
# High-Pass Sharpening  sharpening_kernel = np.array([  
[0, -1, 0],  
[-1, 5, -1],  
[0, -1, 0] 
], dtype=np.float32)    
sharpened = cv2.filter2D(image, -1, sharpening_kernel) 
print("IMAGE 1 - ORIGINAL")  
cv2_imshow(image)
print("IMAGE 1 - GAUSSIAN")  
cv2_imshow(gaussian)
print("IMAGE 1 - AVERAGING") 
cv2_imshow(averaging)
print("IMAGE 1 - MEDIAN")  
cv2_imshow(median) 
print("IMAGE 1 - SHARPENED")  
cv2_imshow(sharpened)  




import cv2  
import numpy as np 
import cv2_imshow  
image = cv2.imread('/Screenshot 2026-09-09 101158.png') 
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
print("IMAGE 2 - ORIGINAL") 
cv2_imshow(image)  
print("IMAGE 2 - GAUSSIAN")  
cv2_imshow(gaussian) 
print("IMAGE 2 - AVERAGING")  
cv2_imshow(averaging) 
print("IMAGE 2 - MEDIAN") 
cv2_imshow(median)  
print("IMAGE 2 - SHARPENED")  
cv2_imshow(sharpened)  


import cv2 
import numpy as np  
import cv2_imshow 
image = cv2.imread('/Screenshot 2026-09-09 101559.png') 
gaussian_kernel = cv2.getGaussianKernel(5, 1.5) 
gaussian_kernel = np.outer(gaussian_kernel, gaussian_kernel) 
gaussian = cv2.filter2D(image, -1, gaussian_kernel)
kernel = np.ones((5, 5), dtype=np.float32) / 25 
averaging = cv2.filter2D(image, -1, kernel) 
median = cv2.medianBlur(image, 5) 
sharpening_kernel = np.array([  
[0, -1, 0],  
[-1, 5, -1],  
[0, -1, 0]  ], dtype=np.float32)  
sharpened = cv2.filter2D(image, -1, sharpening_kernel)
print("IMAGE 3 - ORIGINAL") 
cv2_imshow(image) 
print("IMAGE 3 - GAUSSIAN") 
cv2_imshow(gaussian) 
print("IMAGE 3 - AVERAGING") 
cv2_imshow(averaging) 
print("IMAGE 3 - MEDIAN") 
cv2_imshow(median)  
print("IMAGE 3 - SHARPENED") 
cv2_imshow(sharpened)  


import cv2  
import numpy as np
import cv2_imshow
image = cv2.imread('/Screenshot 2026-09-09 102035.png')
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
print("IMAGE 5 - ORIGINAL")  
cv2_imshow(image)
print("IMAGE 5 - GAUSSIAN")
cv2_imshow(gaussian)
print("IMAGE 5 - AVERAGING")
cv2_imshow(averaging) 
print("IMAGE 5 - MEDIAN") 
cv2_imshow(median)  
print("IMAGE 5 - SHARPENED")
cv2_imshow(sharpened)  


import cv2
import numpy as np
from google.colab.patches 
import cv2_imshow 
 
image=cv2.imread('/Screenshot 2026-09-09 102455.png')
gaussian_kernel = cv2.getGaussianKernel(5, 1.5)
gaussian_kernel = np.outer(gaussian_kernel, gaussian_kernel)
gaussian = cv2.filter2D(image, -1, gaussian_kernel) 
 
kernel = np.ones((5,5), dtype=np.float32)/25 
averaging = cv2.filter2D(image, -1, kernel) 
 
median = cv2.medianBlur(image, 5) 
 
sharpening_kernel = np.array([ 
[0,-1,0], 
[-1,5,-1], 
[0, -1,0] 
], dtype=np.float32) 
 
sharpened =cv2.filter2D(image, -1, sharpening_kernel) 
 
print("IMAGE 6 - ORIGINAL")
cv2_imshow(image) 
 
print("IMAGE 6 - GAUSSIAN") 
cv2_imshow(gaussian) 
 
print("IMAGE 6 - AVERAGING") 
cv2_imshow(averaging) 
 
print("IMAGE 6 - MEDIAN")   
cv2_imshow(median) 
 
print("IMAGE 6 - SHARPENED") 
cv2_imshow(sharpened) 
