# OpenCV 라이브러리를 cv2라는 별칭으로 가져옵니다.
import cv2
# Numpy 라이브러리를 np라는 별칭으로 가져옵니다.
import numpy as np

# 'tracking2.avi' 동영상 파일을 열어서 cap 객체에 저장합니다.
cap = cv2.VideoCapture('tracking2.avi')

# 동영상 파일이 성공적으로 열려있는 동안 계속 반복합니다.
while(cap.isOpened()):
    # 동영상에서 한 프레임씩 읽어옵니다. 
    # _ 에는 읽기 성공 여부(True/False), frame에는 현재 프레임 이미지가 저장됩니다.
    _, frame = cap.read()
    
    # BGR 색상 모델의 프레임을 HSV(색상, 채도, 명도) 색상 모델로 변환합니다.
    # HSV 모델은 특정 색상을 추출하기에 더 용이합니다.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # # 주석에는 파란색(blue)으로 되어 있지만, 실제 HSV 값 범위는 노란색-초록색 계열입니다.
    # (참고: OpenCV에서 파란색의 Hue(색상) 값은 보통 110-130 범위입니다.)
    # 추출할 색상의 하한값(lower)을 HSV로 정의합니다.
    lower_blue = np.array([10,128,128])
    # 추출할 색상의 상한값(upper)을 HSV로 정의합니다.
    upper_blue = np.array([60,255,255])
    
    # hsv 이미지에서 lower_blue와 upper_blue 사이의 값에 해당하는 픽셀을 찾습니다.
    # 범위에 속하는 픽셀은 흰색(255), 나머지는 검은색(0)으로 만드는 마스크(mask) 이미지를 생성합니다.
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # 원본 프레임(frame)과 마스크(mask) 이미지에 비트 AND 연산을 적용합니다.
    # 마스크에서 흰색인 영역만 원본 프레임의 색상이 그대로 나오고, 나머지는 검은색이 됩니다.
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    # 'frame' 창에 원본 영상을 표시합니다.
    cv2.imshow('frame',frame)
    # 'mask' 창에 색상 범위에 따라 생성된 마스크를 표시합니다.
    cv2.imshow('mask',mask)
    # 'res' 창에 최종 결과(추출된 색상 영역만 보이는 영상)를 표시합니다.
    res = cv2.imshow('res',res)
    
    # 5ms 동안 키 입력을 기다립니다.
    k = cv2.waitKey(5) & 0xFF
    # 만약 ESC 키(ASCII 27)가 눌렸다면,
    if k == 27:
        # 반복문을 종료합니다.
        break

# 프로그램 종료 시, 열려있는 모든 OpenCV 창을 닫습니다.
cv2.destroyAllWindows()