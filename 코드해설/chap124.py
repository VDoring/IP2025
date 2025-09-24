# OpenCV 라이브러리를 cv2라는 별칭으로 가져옵니다.
import cv2
# Numpy 라이브러리를 np라는 별칭으로 가져옵니다.
import numpy as np

# 그리기 상태를 저장하는 변수. 마우스가 눌렸을 때 True가 됩니다.
drawing = False 
# 그리기 모드를 설정하는 변수. True이면 사각형, False이면 자유 곡선(원)을 그립니다.
mode = True 
# 마우스를 처음 눌렀을 때의 좌표를 저장할 변수입니다.
ix,iy = -1,-1

# 마우스 이벤트 처리를 위한 콜백 함수 정의
def draw_circle(event,x,y,flags,param):
    # 함수 외부의 전역 변수를 사용하기 위해 global 키워드를 사용합니다.
    global ix,iy,drawing,mode

    # 이벤트가 '마우스 왼쪽 버튼 누름'일 경우
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True  # 그리기 상태를 True로 변경
        ix,iy = x,y     # 현재 마우스 좌표를 시작 좌표(ix,iy)로 저장

    # 이벤트가 '마우스 이동'일 경우
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:  # 마우스가 눌린 상태로 움직이면(드래그)
            if mode == True: # 모드가 사각형 모드이면
                # 시작 좌표부터 현재 좌표까지 초록색 사각형을 채워서(-1) 그립니다.
                # (이 부분은 드래그하는 동안 계속 갱신되지만, 최종 그림은 마우스를 뗄 때 그려집니다)
                # 드래그하는 과정을 실시간으로 보려면 원본 이미지를 계속 복사해서 그려야 합니다.
                pass 
            else: # 모드가 자유 곡선 모드이면
                # 현재 마우스 위치에 반지름 5인 빨간색 원을 채워서(-1) 그립니다.
                cv2.circle(img,(x,y),5,(0,0,255),-1)

    # 이벤트가 '마우스 왼쪽 버튼 뗌'일 경우
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False # 그리기 상태를 False로 변경
        if mode == True: # 모드가 사각형 모드이면
            # 시작 좌표부터 마우스를 뗀 현재 좌표까지 초록색 사각형을 채워서(-1) 그립니다.
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else: # 모드가 자유 곡선 모드이면
            # 마우스를 뗀 위치에 반지름 5인 빨간색 원을 채워서(-1) 그립니다.
            cv2.circle(img,(x,y),5,(0,0,255),-1)

# # (주석 처리된 라인) 512x512 크기의 검은색 이미지를 생성합니다.
# img = np.zeros((512,512,3), np.uint8)

# 'dog.jpg' 파일을 이미지로 불러옵니다.
img = cv2.imread('dog.jpg')
# 원본 이미지를 org 변수에 복사해 둡니다. (나중에 초기화할 때 사용)
org = img.copy()

# 'image'라는 이름의 창을 생성합니다.
cv2.namedWindow('image')
# 'image' 창에서 마우스 이벤트가 발생하면 draw_circle 함수가 호출되도록 설정합니다.
cv2.setMouseCallback('image',draw_circle)

# 무한 루프를 시작합니다.
while(1):
    # 'image' 창에 현재 img 변수의 이미지를 보여줍니다.
    cv2.imshow('image',img)
    # 1ms 동안 키 입력을 기다리고, 입력된 키의 ASCII 값(하위 8비트)을 k에 저장합니다.
    k = cv2.waitKey(1) & 0xFF 
    
    if k == ord('m'): # 'm' 키가 눌렸다면
        mode = not mode # 그리기 모드를 토글합니다 (사각형 <-> 자유 곡선)
    elif k == ord('c'): # 'c' 키가 눌렸다면 (clear)
        img = org.copy() # 이미지를 저장해 둔 원본으로 되돌려 그린 내용을 모두 지웁니다.
    elif k == 27: # ESC 키(ASCII 27)가 눌렸다면
        break # 무한 루프를 종료합니다.

# 프로그램 종료 전, 열려있는 모든 OpenCV 창을 닫습니다.
cv2.destroyAllWindows()