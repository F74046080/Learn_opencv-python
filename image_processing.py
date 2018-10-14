import cv2
import numpy as np

# read image
dog = cv2.imread('images/dog.bmp', 1)
cv2.imshow('dog', dog)
print("Height: " + str(dog.shape[0]) + "\nWidth: " + str(dog.shape[1]))

# chnage the rgb channel
color = cv2.imread('images/color.png', 1)
cv2.imshow('color_rgb', color)
color_new = color[..., [1, 2, 0]]
cv2.imshow('color_rgb_conversion', color_new)

# flip the image 
dog = cv2.imread('images/dog.bmp', 1)
dog_ver = cv2.flip( dog, 1)
cv2.imshow('flip', dog_ver)

cv2.waitKey(0)
