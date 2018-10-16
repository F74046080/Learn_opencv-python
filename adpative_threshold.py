import cv2
import numpy as np

# Read image as gray level
qrcode = cv2.imread('images/QR.png', 0)
cv2.imshow('origin', qrcode)

_, global_threshold = cv2.threshold(qrcode, 80, 255, cv2.THRESH_BINARY)
cv2.imshow('global', global_threshold)

local_threshold_mean = cv2.adaptiveThreshold(qrcode, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 19, -1)
cv2.imshow('local_m', local_threshold_mean)
# local_threshold_gaussian = cv2.adaptiveThreshold(qrcode, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 19, -1)
# cv2.imshow('local_g', local_threshold_gaussian)

cv2.waitKey(0)