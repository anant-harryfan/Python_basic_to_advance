import cv2
import numpy as np

img = cv2.imread('Tut6_cards.jpg')

width, height = 250, 350

pts1 = np.float32([[63, 120], [156, 104], [84, 264], [191, 241]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
# print(pts1[0][0])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))


for x in range(0, 4):
    cv2.circle(img, (int(pts1[x][0]), int(pts1[x][1])), 5, (0, 0, 255), cv2.FILLED)

cv2.imshow("Original image", img)
cv2.imshow("Output image", imgOutput)
cv2.waitKey(0)