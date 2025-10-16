import cv2
import numpy as np

img1 = cv2.imread('1re.jpg', cv2.IMREAD_GRAYSCALE)
cap2 = cv2.VideoCapture('2re.mp4')

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
cv2.imshow('img1', img1)

while (cap2.isOpened()):
    ret, frame2 = cap2.read()
    if ret:
        img2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        kp2, des2 = orb.detectAndCompute(img2, None)
        if des2 is not None and len(des1) > 0 and len(des2) > 0:
            matches = bf.match(des1, des2)
            matches = sorted(matches, key=lambda x: x.distance)
            num_matches_to_draw = min(50, len(matches))
            matching_result = cv2.drawMatches(img1, kp1, frame2, kp2,
                                              matches[:num_matches_to_draw], None, flags=2)
            cv2.imshow('match', matching_result)
        else:
            cv2.imshow('match', frame2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap2.release()
cv2.destroyAllWindows()