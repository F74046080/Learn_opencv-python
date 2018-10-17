import cv2
import numpy as np
from scipy.ndimage.filters import generic_filter

screw = cv2.imread('images/M8.jpg', 0)
# cv2.imshow('screw', screw)

# gaussian smooth
screw_smooth = cv2.GaussianBlur(screw,(5,5),0)
cv2.imshow('smooth', screw_smooth)

def sobel_y(P):
    return np.abs((P[0] + 2 * P[1] + P[2]) - (P[6] + 2 * P[7] + P[8]))
def sobel_x(P):
    return np.abs((P[2] + 2 * P[6] + P[7]) - (P[0] + 2 * P[3] + P[6]))
def sobel(P):
    return (np.abs((P[0] + 2 * P[1] + P[2]) - (P[6] + 2 * P[7] + P[8])) +
            np.abs((P[2] + 2 * P[6] + P[7]) - (P[0] + 2 * P[3] + P[6])))
screw_sobely = generic_filter(screw_smooth, sobel_y, (3, 3))
cv2.imshow('sobel_y', screw_sobely)
screw_sobelx = generic_filter(screw_smooth, sobel_x, (3, 3))
cv2.imshow('sobel_x', screw_sobelx)
screw_sobel = generic_filter(screw_smooth, sobel, (3, 3))
cv2.imshow('sobel', screw_sobel)
cv2.waitKey(0)