import cv2
import numpy as np

a = cv2.imread('images/OriginalTransform.png')
cv2.imshow('origin', a)
print(a.shape)
# rows -> height  columns -> width
rows, cols, channel = a.shape

# translation position
tx = 150
ty = 50
translation = np.float32([[1, 0, tx], [0, 1, ty]])
tra_dst = cv2.warpAffine(a, translation, (cols, rows))
cv2.imshow('img',tra_dst)

rotate = cv2.getRotationMatrix2D((130+tx, 125+ty), 45, 2)
rot_dst = cv2.warpAffine(tra_dst, rotate, (cols, rows))
cv2.imshow('rotate', rot_dst)


cv2.waitKey(0)
