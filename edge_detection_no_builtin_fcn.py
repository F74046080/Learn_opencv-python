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
# cv2.imshow('sobel_y', screw_sobely)
screw_sobelx = generic_filter(screw_smooth, sobel_x, (3, 3))
# cv2.imshow('sobel_x', screw_sobelx)
screw_sobel = generic_filter(screw_smooth, sobel, (3, 3))
cv2.imshow('sobel', screw_sobel)

ret,screw_threshold = cv2.threshold(screw_sobel, 100, 255, cv2.THRESH_BINARY)
# cv2.imshow('threshold', screw_threshold)
np.set_printoptions(threshold=np.nan)
# print(np.where(screw_threshold < 0))
def magnitude_threshold(x):
    magnitude_value = cv2.getTrackbarPos('bar','magnitude')    
    ret,screw_threshold = cv2.threshold(screw_sobel, magnitude_value, 255, cv2.THRESH_BINARY)
    cv2.imshow('magnitude', screw_threshold)

cv2.namedWindow('magnitude')
cv2.createTrackbar('bar', 'magnitude', 40, 255, magnitude_threshold)
ret,screw_threshold = cv2.threshold(screw_sobel, 40, 255, cv2.THRESH_BINARY)
cv2.imshow('magnitude', screw_threshold)

# direction
def direction_threshold(x):
    theta = cv2.getTrackbarPos('theta','direction')
    theta_mat_cp = theta_mat.copy()
    for i in range(theta_mat_cp.shape[0]):
        for j in range(theta_mat_cp.shape[1]):
            if theta_mat_cp[i][j] > (theta+10) or theta_mat_cp[i][j] < (theta-10):
                theta_mat_cp[i][j] = 0
            else:
                theta_mat_cp[i][j] = 1
    screw_direction = np.multiply(theta_mat_cp, screw_sobel)
    cv2.imshow('direction', screw_direction)

cv2.namedWindow('direction')
cv2.createTrackbar('theta', 'direction', 10, 360, direction_threshold)
theta_mat = np.arctan2(screw_sobely, screw_sobelx)*180/np.pi
theta_mat = theta_mat.astype(np.uint8)
theta = 10
theta_mat_cp = theta_mat.copy()
for i in range(theta_mat_cp.shape[0]):
    for j in range(theta_mat_cp.shape[1]):
        if theta_mat_cp[i][j] > (theta+10) or theta_mat_cp[i][j] < (theta-10):
            theta_mat_cp[i][j] = 0
        else:
            theta_mat_cp[i][j] = 1
screw_direction = np.multiply(theta_mat_cp, screw_sobel)
cv2.imshow('direction', screw_direction)

# # theta_mat = np.degrees(np.arctan2(screw_sobely, screw_sobelx))
# theta_mat = np.arctan2(screw_sobely, screw_sobelx)*180/np.pi
# theta_mat = theta_mat.copy().astype(np.uint8)
# # print(screw_sobelx.shape)
# # print(theta_mat.shape)
# # print(np.where(theta_mat > 20))
# print(theta_mat[0])
# theta = 10
# for i in range(theta_mat.shape[0]):
#     for j in range(theta_mat.shape[1]):
#         if theta_mat[i][j] > (theta+10) or theta_mat[i][j] < (theta-10):
#             theta_mat[i][j] = 0
#         else:
#             theta_mat[i][j] = 1
# # theta_mat[theta_mat[i] <= (theta+10)] = 1
# # theta_mat[theta_mat[i] <  (theta-10)] = 0 
# # print(np.where(theta_mat == 1))
# # screw_direction = screw_sobel.copy()
# print(theta_mat)
# screw_direction = np.multiply(theta_mat, screw_sobel)
# screw_direction2 = screw_direction.copy()

# # print(np.where(screw_direction > 100))
# # print(screw_direction2.dtype)
# # print(screw_direction2.shape)
# # print(type(screw_direction2))
# # print(screw_sobel.shape)
# # print(type(screw_sobel))
# cv2.imshow('Direction', screw_direction2)
# print(np.array_equal(screw_direction2, screw_sobel))
# # cv2.imshow('Direction', cv2.bitwise_and(theta_mat,screw_direction))
# # def direction_threshold(x):
# #     theta = cv2.getTrackbarPos('theta', 'orientation')
# # cv2.namedWindow('orientation')
# # cv2.createTrackbar('theta', 'orientation', 40, 255, direction_threshold)

cv2.waitKey(0)