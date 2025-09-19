import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dsu3.jpg')
rows,cols,ch = img.shape
pts1 = np.float32([[105,228],[700,163],[112,496],[705,540]])
pts2 = np.float32([[0,0],[600,0],[0,300],[600,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
print(M)
dst = cv2.warpPerspective(img,M,(600,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
