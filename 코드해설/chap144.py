# OpenCV 라이브러리를 cv2라는 별칭으로 가져옵니다.
import cv2
# Numpy 라이브러리를 np라는 별칭으로 가져옵니다.
import numpy as np
# Matplotlib의 pyplot 모듈을 plt라는 별칭으로 가져와 이미지 표시에 사용합니다.
from matplotlib import pyplot as plt

# 'OpenCV_noise.png'라는 노이즈가 포함된 이미지 파일을 읽어옵니다.
img = cv2.imread('OpenCV_noise.png')

# 필터링에 사용할 커널(kernel)의 크기를 변수 k에 저장합니다.
k=5

# 가우시안 블러(GaussianBlur)를 적용합니다.
# (k,k) 즉, (5,5) 크기의 커널을 사용하여 이미지를 부드럽게 만듭니다.
blur = cv2.GaussianBlur(img,(k,k),0)

# 미디언 블러(medianBlur)를 적용합니다.
# k 즉, 5x5 크기 커널 내 픽셀들의 중간값을 찾아 현재 픽셀 값으로 대체합니다.
median = cv2.medianBlur(img,k)

# Matplotlib을 사용하여 두 결과를 나란히 비교합니다.
# 1행 2열 그리드의 첫 번째(121) 위치에 미디언 블러 결과를 표시합니다.
plt.subplot(121),plt.imshow(median),plt.title('median')
# x, y축의 눈금을 제거합니다.
plt.xticks([]), plt.yticks([])

# 1행 2열 그리드의 두 번째(122) 위치에 가우시안 블러 결과를 표시합니다.
plt.subplot(122),plt.imshow(blur),plt.title('gaussian blur')
# x, y축의 눈금을 제거합니다.
plt.xticks([]), plt.yticks([])

# 위에서 설정한 모든 플롯을 창에 나타냅니다.
plt.show()