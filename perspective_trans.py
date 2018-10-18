import cv2
import numpy as np
# cv2.namedWindow('origin', cv2.WINDOW_NORMAL)
orig = cv2.imread('images/OriginalPerspective.png')
# cv2.imshow('origin', orig)
orig_resize = cv2.resize(orig, (1200, 900))
cv2.imshow('origin', orig_resize)
# cv2.namedWindow('perspective transformation')
positions = []
def mousePosition(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(x,y)
        positions.append([x*1.3333, y*1.3333])
        # positions.append([round(x*1.3333), round(y*1.3333)])
        if len(positions) == 4:
            # new_pos = [i * 1.3 for i in positions]
            # pts1 = np.float32([new_pos[0], new_pos[1], new_pos[3], new_pos[2]])

            pts1 = np.float32([positions[0], positions[1], positions[3], positions[2]])
            pts2 = np.float32([[20, 20], [450, 20], [20, 450], [450, 450]])
            # pts2 = np.float32([[0, 0], [450, 0], [0, 450], [450, 450]])

            M = cv2.getPerspectiveTransform(pts1, pts2)

            dst = cv2.warpPerspective(orig , M, (450, 450))
            cv2.imshow('after', dst)
            positions.clear()
            # positions.append([x, y])

cv2.setMouseCallback('origin', mousePosition )
# pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
# pts2 = np.float32([[20, 20], [450, 20], [20, 450], [450, 450]])

# M = cv2.getPerspectiveTransform(pts1, pts2)

# dst = cv2.warpPerspective(orig , M, (430, 430))
# cv2.imshow('after', dst)
cv2.waitKey(0)