# OpenCV 라이브러리를 cv2라는 별칭으로 가져옵니다.
import cv2
# Numpy 라이브러리를 np라는 별칭으로 가져옵니다.
import numpy as np
# Matplotlib의 pyplot 모듈을 plt라는 별칭으로 가져와 이미지 표시에 사용합니다.
from matplotlib import pyplot as plt

# 'dsu3.jpg' 이미지 파일을 읽어옵니다.
img = cv2.imread('dsu3.jpg')
# 이미지의 높이, 너비, 채널 수를 가져옵니다. (이 코드에서는 직접 사용되진 않습니다.)
rows,cols,ch = img.shape

# 원본 이미지에서 변환의 기준이 될 4개의 점 좌표를 지정합니다.
# 순서는 보통 좌상단, 우상단, 좌하단, 우하단 입니다. (float32 형태로 지정)
pts1 = np.float32([[105,228],[700,163],[112,496],[705,540]])

# pts1의 점들이 매핑될 결과 이미지에서의 4개의 점 좌표를 지정합니다.
# 여기서는 600x300 크기의 직사각형 꼭짓점들입니다.
pts2 = np.float32([[0,0],[600,0],[0,300],[600,300]])

# pts1 좌표를 pts2 좌표로 변환하는 3x3 원근 변환 행렬(M)을 계산합니다.
M = cv2.getPerspectiveTransform(pts1,pts2)
# 계산된 변환 행렬을 콘솔에 출력합니다.
print(M)

# 원본 이미지(img)에 변환 행렬(M)을 적용하여 원근 변환을 수행합니다.
# 결과 이미지의 크기는 (너비, 높이) 순으로 (600, 300)으로 설정합니다.
dst = cv2.warpPerspective(img,M,(600,300))

# Matplotlib을 사용하여 원본과 결과를 나란히 표시합니다.
# 1행 2열 그리드의 첫 번째(121) 위치에 원본 이미지를 표시합니다.
plt.subplot(121),plt.imshow(img),plt.title('Input')
# 1행 2열 그리드의 두 번째(122) 위치에 결과 이미지를 표시합니다.
plt.subplot(122),plt.imshow(dst),plt.title('Output')

# 위에서 설정한 모든 플롯을 창에 나타냅니다.
plt.show()