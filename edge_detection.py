import cv2
import numpy as np

# loading image in gray level
img = cv2.imread('images/M8.jpg', 0)
cv2.imshow('origin gray level', img)

# remove noise
img_rmnoise = cv2.GaussianBlur(img, (3,3), 0)
cv2.imshow('remove the noise', img_rmnoise)

# convolute with proper kernels
laplacian = cv2.Laplacian(img_rmnoise, cv2.CV_64F)
sobelx = cv2.Sobel(img_rmnoise, cv2.CV_64F, 1, 0, ksize=5)  # x
sobely = cv2.Sobel(img_rmnoise, cv2.CV_64F, 0, 1, ksize=5)  # y
sobel = cv2.Sobel(img_rmnoise, cv2.CV_64F, 1, 1, ksize=5)  # y
canny = cv2.Canny(img_rmnoise, 50, 150)

# cv2.imshow('laplacian', laplacian)
# cv2.imshow('sobel x', sobelx)
# cv2.imshow('sobel y', sobely)
cv2.imshow('sobel', sobel)

cv2.waitKey(0)