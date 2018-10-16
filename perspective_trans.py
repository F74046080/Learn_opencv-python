import cv2
import numpy as np

orig = cv2.imread('images/OriginalPerspective.png')
cv2.imshow('origin', orig)

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[20, 20], [450, 20], [20, 450], [450, 450]])

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(orig , M, (430, 430))
cv2.imshow('after', dst)
cv2.waitKey(0)