import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('OpenCV_noise.png')
k=5
blur = cv2.GaussianBlur(img,(k,k),0)
median = cv2.medianBlur(img,k)
plt.subplot(121),plt.imshow(median),plt.title('median')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('gaussian blur')
plt.xticks([]), plt.yticks([])
plt.show()