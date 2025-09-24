# OpenCV 라이브러리를 cv2라는 별칭으로 가져옵니다.
import cv2
# Numpy 라이브러리를 np라는 별칭으로 가져옵니다.
import numpy as np

# 트랙바의 콜백(callback) 함수로 사용될, 아무 동작도 하지 않는 함수입니다.
def nothing(x):
    pass

# 첫 번째 이미지('dog.jpeg')를 불러옵니다.
img1 = cv2.imread('dog.jpeg')
# 두 번째 이미지('opencv_logo_resize.jpg')를 불러옵니다.
# 두 이미지의 크기는 동일해야 합니다.
img2 = cv2.imread('opencv_logo_resize.jpg')

# # (이 줄은 while 루프 안에서 계속 갱신되므로, 초기값을 보여주는 역할만 합니다.)
# # img1에 가중치 0.7, img2에 가중치 0.3을 적용하여 두 이미지를 합성합니다.
# dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

# 'image'라는 이름의 창을 생성합니다.
cv2.namedWindow('image')
# 'image' 창에 'weight'라는 이름의 트랙바를 생성합니다. 범위는 0부터 100까지입니다.
cv2.createTrackbar('weight','image',0,100,nothing)

# 무한 루프를 시작합니다.
while(1):
    # 'weight' 트랙바의 현재 위치(값)를 가져와 100으로 나누어 0.0 ~ 1.0 사이의 가중치(w)로 만듭니다.
    w=cv2.getTrackbarPos('weight','image')/100
    # 현재 가중치 값을 콘솔에 출력합니다.
    print(w)
    
    # addWeighted 함수로 두 이미지를 합성합니다.
    # dst = img1 * w + img2 * (1-w) + 0 (gamma)
    # 트랙바의 값(w)에 따라 두 이미지가 보이는 비율이 조절됩니다.
    dst = cv2.addWeighted(img1, 1-w, img2, w, 0)
    
    # 합성된 결과 이미지(dst)를 'image' 창에 보여줍니다.
    cv2.imshow('image',dst)
    # 1ms 동안 키 입력을 기다립니다.
    k=cv2.waitKey(1)&0xFF
    # 만약 ESC 키(ASCII 27)가 눌렸다면,
    if k==27:
        # 무한 루프를 종료합니다.
        break

# 프로그램 종료 시 모든 OpenCV 창을 닫습니다.
cv2.destroyAllWindows()

# # 아래는 주석 처리된 코드로, 실행되지 않습니다.
# # 단일 이미지를 한 번만 표시하는 기본 코드입니다.
# cv2.imshow('image',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()