import cv2
import numpy as np

# read image
pyramid = cv2.imread('images/pyramids_Gray.jpg')
cv2.imshow('origin', pyramid)

# Gaussian pyramid level 1
g1_pyramid = cv2.pyrDown(pyramid)
cv2.imshow('Gaussian pyramid level 1', g1_pyramid)

# Laplacian pyramid level 0 
g1_expanded = cv2.pyrUp(g1_pyramid)
l0_pyramid = cv2.subtract(pyramid, g1_expanded)
cv2.imshow('Laplacian pyramid level 0', l0_pyramid)

# Laplacian pyramid level 1
g2_pyramid = cv2.pyrDown(g1_pyramid)
g2_expanded = cv2.pyrUp(g2_pyramid)
l1_pyramid = cv2.subtract(g1_pyramid, g2_expanded)

# Inverse pyramid level 1
i2_expanded = g2_expanded.copy()
i1_pyramid = cv2.add(l1_pyramid, i2_expanded)
cv2.imshow('Inverse pyramid level 1', i1_pyramid)

# Inverse pyramid level 0
i1_expanded = cv2.pyrUp(i1_pyramid)
i0_pyramid = cv2.add(l0_pyramid, i1_expanded)
cv2.imshow('Inverse pyramid level 0', i0_pyramid)

cv2.waitKey(0)