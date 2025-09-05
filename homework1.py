import cv2
import numpy as np

drawing = False    
ix, iy = -1, -1   
ex, ey = -1, -1  
mx, my = 0, 0 

def nothing(x):
    pass

def on_mouse(event, x, y, flags, param):
    global drawing, ix, iy, ex, ey, mx, my
    mx, my = x, y

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        ex, ey = x, y

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        ex, ey = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        ex, ey = x, y

img = cv2.imread('mountain.jpg')
base = img.copy()

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('image', on_mouse)
cv2.createTrackbar('value', 'image', 100, 100, nothing)

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    frame = base.copy()

    alpha = cv2.getTrackbarPos('value', 'image') / 100.0

    if ix >= 0 and iy >= 0 and ex >= 0 and ey >= 0:
        x1, y1 = min(ix, ex), min(iy, ey)
        x2, y2 = max(ix, ex), max(iy, ey)

        overlay = frame.copy()
        cv2.rectangle(overlay, (x1, y1), (x2, y2), (0, 0, 255), -1)
        cv2.rectangle(overlay, (x1, y1), (x2, y2), (0, 0, 255), 2)
        frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)

    text = f"Mouse position ({mx},{my})  -  ({ix},{iy})  -  ({ex},{ey})  -  alpha {alpha:.1f}"
    cv2.putText(frame, text, (10, 30), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('image', frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        ix = iy = ex = ey = -1
    elif key == 27:
        break

cv2.destroyAllWindows()
