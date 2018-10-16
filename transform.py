import cv2
import numpy as np

a = cv2.imread('images/OriginalTransform.png')
cv2.imshow('origin', a)
print(a.shape)
# rows -> height   columns -> width
rows, cols, channel = a.shape

# translation position
tx = 150
ty = 50
translation = np.float32([[1, 0, tx], [0, 1, ty]])
tra_dst = cv2.warpAffine(a, translation, (cols, rows))
cv2.imshow('img',tra_dst)


cv2.waitKey(0)
