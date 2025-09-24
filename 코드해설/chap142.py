# OpenCV 라이브러리를 cv2라는 별칭으로 가져옵니다.
import cv2
# Numpy 라이브러리를 np라는 별칭으로 가져옵니다.
import numpy as np
# Matplotlib의 pyplot 모듈을 plt라는 별칭으로 가져와 이미지 및 그래프 표시에 사용합니다.
from matplotlib import pyplot as plt

# 'sIMG_2168.jpg' 이미지를 흑백(grayscale, 채널 0)으로 읽어옵니다.
img = cv2.imread('sIMG_2168.jpg',0)

# 1. 전역 임계값 처리 (Global Thresholding)
# 픽셀 값이 127보다 크면 255(흰색), 작거나 같으면 0(검은색)으로 변환합니다.
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# 2. 오츠(Otsu)의 이진화
# 이미지의 히스토그램을 분석하여 최적의 임계값을 자동으로 찾아 적용합니다.
# 임계값 인자(여기서는 0)는 오츠 알고리즘 사용 시 무시됩니다.
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# 3. 가우시안 필터링 후 오츠의 이진화
# (5,5) 커널을 사용하여 이미지의 노이즈를 제거(블러 처리)합니다.
blur = cv2.GaussianBlur(img,(5,5),0)
# 노이즈가 제거된 이미지에 오츠의 이진화를 적용합니다.
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Matplotlib으로 표시할 이미지와 제목들을 리스트에 정리합니다.
# 히스토그램이 그려질 자리에는 임시로 0을 넣어둡니다.
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

# for문을 사용하여 3가지 경우를 각각 3x3 서브플롯에 그립니다.
for i in range(3):
    # 3x3 그리드의 첫 번째 열 (원본 이미지)
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    
    # 3x3 그리드의 두 번째 열 (히스토그램)
    # .ravel()은 이미지를 1차원 배열로 만들어 히스토그램 계산을 용이하게 합니다.
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    
    # 3x3 그리드의 세 번째 열 (임계값 처리 결과)
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])

# 위에서 설정한 모든 서브플롯을 창에 나타냅니다.
plt.show()