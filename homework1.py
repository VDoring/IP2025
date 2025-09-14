import cv2 
import numpy as np

def nothing(x):
    pass

font = cv2.FONT_HERSHEY_SIMPLEX
img_origin = cv2.imread('mountain.jpg')

drawing = False
mode = True
ix, iy = -1, -1
img = img_origin.copy()
alpha = 0.5

def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode, img, img_origin, alpha

    img = img_origin.copy()

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if y < img.shape[0] and x < img.shape[1]:
            txt = 'Mouse Position (' + str(x) + ',' + str(y) + ')' + str(img_origin[y, x])
        else:
            txt = 'Mouse Position (' + str(x) + ',' + str(y) + ')'
        cv2.putText(img, txt, (30, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        if drawing == True:
            overlay = img.copy()
            if mode == True:
                cv2.rectangle(overlay, (ix, iy), (x, y), (0, 0, 255), -1)
            else:
                cv2.circle(overlay, (x, y), 5, (0, 0, 255), -1)
            img = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        overlay = img_origin.copy()
        if mode == True:
            cv2.rectangle(overlay, (ix, iy), (x, y), (0, 0, 255), -1)
        else:
            cv2.circle(overlay, (x, y), 5, (0, 0, 255), -1)

        img_origin = cv2.addWeighted(overlay, alpha, img_origin, 1 - alpha, 0)
        img = img_origin.copy()

cv2.namedWindow('image')
cv2.createTrackbar('R', 'image', 0, 255, nothing)

cv2.setMouseCallback('image', draw_circle)
while (1):
    r = cv2.getTrackbarPos('R', 'image')
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
        print(f"Mode changed to: {'Rectangle' if mode else 'Circle'}")
    elif k == 27:
        break
cv2.destroyAllWindows()