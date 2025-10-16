import cv2
import numpy as np

img1 = cv2.imread('1re.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('2re.jpg', cv2.IMREAD_GRAYSCALE)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

matching_result = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, flags=2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('match', matching_result)
cv2.waitKey(0)
cv2.destroyAllWindows()