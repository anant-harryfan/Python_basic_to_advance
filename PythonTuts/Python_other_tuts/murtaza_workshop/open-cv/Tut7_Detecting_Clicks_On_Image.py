import cv2
import numpy as np

circles = np.zeros((4, 2), np.int)
counter = 0

def mousePoints(events, x, y, flags, param):
    global counter
    if events == cv2.EVENT_LBUTTONDOWN:
        # print(x, y)
        circles[counter] = x, y
        counter = counter + 1
        print(circles)

img = cv2.imread('Tut1_itachi_uchiha.jpg')
while True:
    if counter == 4:
        width, height = 250, 350
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        # print(pts1[0][0])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("Output Image", imgOutput)


    for z in range(0, 4):
        cv2.circle(img, (int(circles[z][0]), int(circles[z][1])), 3, (0, 0, 255), cv2.FILLED)

    cv2.imshow("Original", img)
    cv2.setMouseCallback("Original", mousePoints)
    cv2.waitKey(1)