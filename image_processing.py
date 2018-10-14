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
dog_ver = cv2.flip(dog, 1)
cv2.imshow('flip', dog_ver)

# blending the image and the flip image
def nothing(x):
    pass
dog1 = cv2.imread('images/dog.bmp', 1)
dog2 = cv2.flip(dog1,1)
cv2.namedWindow('blending')
dog_show = dog1.copy()
# cv2.imshow('test', dog_show)
cv2.createTrackbar('bar', 'blending', 0, 100, nothing)
while (cv2.getWindowProperty('blending', 0) >= 0):
    cv2.imshow('blending', dog_show)
    alpha = cv2.getTrackbarPos('bar','blending')
    dog_show = cv2.addWeighted(dog1, alpha/100, dog2, 1-alpha/100, 0)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.waitKey(0)  