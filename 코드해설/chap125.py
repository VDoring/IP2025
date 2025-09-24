# OpenCV 라이브러리를 cv2라는 별칭으로 가져옵니다.
import cv2
# Numpy 라이브러리를 np라는 별칭으로 가져옵니다.
import numpy as np

# 트랙바가 변경될 때 호출될 콜백(callback) 함수를 정의합니다. 
# cv2.createTrackbar 함수는 콜백 함수를 필수로 요구하지만, 
# 이 코드에서는 특별한 동작이 필요 없으므로 아무것도 하지 않는(pass) 함수를 만듭니다.
def nothing(x):
    pass

# 300x512 크기의 3채널(컬러) 검은색 이미지를 생성합니다.
img = np.zeros((300,512,3), np.uint8)
# 'image'라는 이름의 창을 생성합니다. WINDOW_NORMAL 플래그는 창 크기를 조절할 수 있게 해줍니다.
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

# 'image' 창에 'R'이라는 이름의 트랙바를 생성합니다. 범위는 0부터 255까지이며, 값이 바뀔 때 nothing 함수를 호출합니다.
cv2.createTrackbar('R','image',0,255,nothing)
# 'image' 창에 'G'이라는 이름의 트랙바를 생성합니다. 범위는 0부터 255까지입니다.
cv2.createTrackbar('G','image',0,255,nothing)
# 'image' 창에 'B'이라는 이름의 트랙바를 생성합니다. 범위는 0부터 255까지입니다.
cv2.createTrackbar('B','image',0,255,nothing)

# 스위치 역할을 할 트랙바의 이름으로 사용할 문자열을 정의합니다.
switch = '0 : OFF \n1 : ON'
# 'image' 창에 스위치 트랙바를 생성합니다. 범위는 0(OFF)부터 1(ON)까지입니다.
cv2.createTrackbar(switch, 'image',0,1,nothing)

# 무한 루프를 시작하여 실시간으로 변경사항을 확인하고 적용합니다.
while(1):
    # 'image' 창에 현재 img 이미지를 표시합니다.
    cv2.imshow('image',img)
    # 1ms 동안 키 입력을 기다리고, 입력된 키의 ASCII 값(하위 8비트)을 k에 저장합니다.
    k = cv2.waitKey(1) & 0xFF
    # 만약 입력된 키가 ESC 키(ASCII 27)이면,
    if k == 27:
        break # 무한 루프를 종료합니다.

    # 'R' 트랙바의 현재 위치(값)를 가져옵니다.
    r = cv2.getTrackbarPos('R','image')
    # 'G' 트랙바의 현재 위치(값)를 가져옵니다.
    g = cv2.getTrackbarPos('G','image')
    # 'B' 트랙바의 현재 위치(값)를 가져옵니다.
    b = cv2.getTrackbarPos('B','image')
    # 스위치 트랙바의 현재 위치(값)를 가져옵니다.
    s = cv2.getTrackbarPos(switch,'image')

    # 만약 스위치가 0 (OFF)이면
    if s == 0:
        img[:] = 0 # 이미지 전체를 검은색(0)으로 채웁니다.
    # 스위치가 1 (ON)이면
    else:
        # 이미지 전체를 트랙바에서 가져온 [B, G, R] 값으로 채웁니다. (OpenCV는 BGR 순서)
        img[:] = [b,g,r]

# 프로그램이 종료될 때, 열려있는 모든 OpenCV 창을 닫습니다.
cv2.destroyAllWindows()