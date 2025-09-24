# OpenCV 라이브러리를 cv2라는 별칭으로 가져옵니다.
import cv2
# Numpy 라이브러리를 np라는 별칭으로 가져옵니다.
import numpy as np

# 트랙바의 콜백 함수로 사용될, 아무 동작도 하지 않는 함수입니다.
def nothing(x):
    pass

# 텍스트를 표시할 때 사용할 폰트를 설정합니다.
font = cv2.FONT_HERSHEY_SIMPLEX
# 'mountain.png' 이미지 파일을 불러와 원본 이미지 변수에 저장합니다.
img_origin = cv2.imread('mountain.png')
# 그리기 상태를 저장하는 변수 (마우스가 눌리면 True)
drawing=False
# 그리기 모드를 설정하는 변수 (True: 사각형, False: 원)
mode= True
# 마우스를 처음 눌렀을 때의 좌표를 저장할 변수
ix,iy=-1,-1
# 실제 화면에 표시하고 그림을 그릴 이미지를 원본 이미지의 복사본으로 생성합니다.
img = img_origin.copy()

# 마우스 이벤트 처리를 위한 콜백 함수
def draw_circle(event,x,y,flags,param):
    # 함수 외부의 전역 변수들을 사용하기 위해 global로 선언합니다.
    global ix,iy,drawing,mode,img
    # 마우스 이벤트가 발생할 때마다 이미지를 원본으로 초기화하여 이전 프레임의 그림을 지웁니다.
    img = img_origin.copy()
    
    if event==cv2.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼을 눌렀을 때
        drawing=True # 그리기 상태를 True로 변경
        ix,iy=x,y # 현재 좌표를 시작 좌표로 저장
        
    elif event==cv2.EVENT_MOUSEMOVE: # 마우스를 움직일 때
        # 'Mouse Position (x,y)[B,G,R]' 형태의 문자열을 생성합니다.
        txt = 'Mouse Position ('+str(x)+','+str(y)+')'+str(img[y,x])
        # 생성한 문자열을 이미지의 (30,30) 위치에 흰색으로 표시합니다.
        cv2.putText(img,txt,(30,30), font, 1,(255,255,255),2,cv2.LINE_AA)
        
        if drawing==True: # 마우스가 눌린 상태로 움직일 때 (드래그)
            if mode== True: # 사각형 모드일 경우
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1) # 시작점부터 현재까지 초록색 사각형을 채워서 그림
            else: # 원(자유곡선) 모드일 경우
                cv2.circle(img,(x,y),5,(0,0,255),-1) # 현재 위치에 반지름 5의 빨간색 원을 채워서 그림
                
    elif event==cv2.EVENT_LBUTTONUP: # 마우스 왼쪽 버튼을 뗄 때
        drawing=False # 그리기 상태를 False로 변경
        if mode== True: # 사각형 모드일 경우
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1) # 최종 사각형을 그림
        else: # 원 모드일 경우
            cv2.circle(img,(x,y),5,(0,0,255),-1) # 최종 원을 그림

# 'image'라는 이름의 창을 생성합니다.
cv2.namedWindow('image')
# 'image' 창에 'R'이라는 트랙바를 생성합니다. (이 코드에서는 실제로 사용되진 않습니다.)
cv2.createTrackbar('R','image',0,255,nothing)

# 'image' 창에 마우스 이벤트가 발생하면 draw_circle 함수가 호출되도록 설정합니다.
cv2.setMouseCallback('image',draw_circle)

# 무한 루프를 시작합니다.
while(1):
    # 'R' 트랙바의 현재 값을 읽어옵니다.
    r=cv2.getTrackbarPos('R','image')
    # 읽어온 값을 콘솔에 출력합니다.
    print(r)
    # 'image' 창에 현재 이미지를 표시합니다.
    cv2.imshow('image',img)
    # 1ms 동안 키 입력을 기다립니다.
    k=cv2.waitKey(1)&0xFF
    
    if k== ord('m'): # 'm' 키를 누르면
        mode=not mode # 그리기 모드를 토글 (사각형 <-> 원)
    elif k==27: # ESC 키를 누르면
        break # 무한 루프를 종료합니다.

# 프로그램 종료 시 모든 OpenCV 창을 닫습니다.
cv2.destroyAllWindows()

""" 
# 아래는 여러 줄 주석으로, 실행되지 않는 코드 블록입니다.
# 이미지의 특정 영역(Region of Interest, ROI)의 픽셀 값을 조작하는 예제입니다.

cv2.namedWindow('image')
# 이미지의 y좌표 100~199, x좌표 100~199 영역의 Blue 채널(인덱스 2) 값을 255로 변경합니다.
img[100:200, 100:200, 2] = 255 
while(1):
    cv2.imshow('image', img)
    k=cv2.waitKey(1)&0xFF
    if k == 27:
        break
cv2.destroyAllWindows() 
"""