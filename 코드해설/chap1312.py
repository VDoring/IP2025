# OpenCV 라이브러리를 cv2라는 별칭으로 가져옵니다.
import cv2
# Numpy 라이브러리를 np라는 별칭으로 가져옵니다.
import numpy as np
# Matplotlib의 pyplot 모듈을 plt라는 별칭으로 가져와 이미지 및 그래프 표시에 사용합니다.
from matplotlib import pyplot as plt

# 테두리 색상으로 사용할 값을 리스트로 정의합니다. 
# OpenCV는 BGR 순서이므로 [0, 255, 0]은 초록색(Green)입니다.
BLUE = [0,255,0] 

# 'opencv_logo.jpg' 이미지 파일을 읽어옵니다.
img1 = cv2.imread('opencv_logo.jpg')

# cv2.copyMakeBorder() 함수로 다양한 테두리를 생성합니다.
# 인자는 순서대로 (이미지, top, bottom, left, right, 테두리 타입, 색상값) 입니다.

# BORDER_REPLICATE: 가장자리 픽셀을 복제하여 테두리를 채웁니다. (예: aaaa|abcd|dddd)
replicate = cv2.copyMakeBorder(img1,50,50,50,50,cv2.BORDER_REPLICATE)

# BORDER_REFLECT: 거울에 비친 것처럼 픽셀을 반사하여 테두리를 채웁니다. (예: dcb|abcd|cba)
reflect = cv2.copyMakeBorder(img1,50,50,50,50,cv2.BORDER_REFLECT)

# BORDER_REFLECT_101: 가장자리 픽셀을 제외하고 반사합니다. BORDER_REFLECT와 유사하지만 경계가 더 자연스럽습니다. (예: cba|abcd|bcd)
reflect101 = cv2.copyMakeBorder(img1,50,50,50,50,cv2.BORDER_REFLECT_101)

# BORDER_WRAP: 이미지의 반대쪽 끝부분을 가져와 테두리를 채웁니다. (예: bcd|abcd|abc)
wrap = cv2.copyMakeBorder(img1,50,50,50,50,cv2.BORDER_WRAP)

# BORDER_CONSTANT: 지정된 상수 값(색상)으로 테두리를 채웁니다. 여기서는 위에서 정의한 초록색을 사용합니다.
constant= cv2.copyMakeBorder(img1,50,50,50,50,cv2.BORDER_CONSTANT,value=BLUE)

# Matplotlib을 사용하여 여러 이미지를 한 번에 표시합니다.
# 2행 3열의 서브플롯 중 첫 번째(231) 위치에 원본 이미지를 표시하고 제목을 설정합니다.
# 참고: OpenCV는 BGR, Matplotlib은 RGB 순서이므로 색상이 다르게 보일 수 있습니다.
plt.subplot(231),plt.imshow(img1),plt.title('ORIGINAL')

# 두 번째(232) 위치에 REPLICATE 결과를 표시합니다.
plt.subplot(232),plt.imshow(replicate),plt.title('REPLICATE')

# 세 번째(233) 위치에 REFLECT 결과를 표시합니다.
plt.subplot(233),plt.imshow(reflect),plt.title('REFLECT')

# 네 번째(234) 위치에 REFLECT_101 결과를 표시합니다.
plt.subplot(234),plt.imshow(reflect101),plt.title('REFLECT_101')

# 다섯 번째(235) 위치에 WRAP 결과를 표시합니다.
plt.subplot(235),plt.imshow(wrap),plt.title('WRAP')

# 여섯 번째(236) 위치에 CONSTANT 결과를 표시합니다.
plt.subplot(236),plt.imshow(constant),plt.title('CONSTANT')

# 위에서 설정한 모든 서브플롯을 창에 나타냅니다.
plt.show()