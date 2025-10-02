import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('messi5.jpg',0)
# edges = cv2.Canny(img,100,200)
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()

img = cv2.imread('Lenna.png',0)
edges1 = cv2.Canny(img,50,200)
edges2 = cv2.Canny(img,100,200)
edges3 = cv2.Canny(img,150,200)
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(edges1,cmap = 'gray')
plt.title('50,200'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(edges2,cmap = 'gray')
plt.title('100,200'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(edges3,cmap = 'gray')
plt.title('150,200'), plt.xticks([]), plt.yticks([])
plt.show()