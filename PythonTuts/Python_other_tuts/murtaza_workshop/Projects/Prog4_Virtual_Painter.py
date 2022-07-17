import numpy
import numpy as np
from cvzone.ColorModule import ColorFinder
from cvzone.HandTrackingModule import HandDetector
from cvzone import stackImages
import cv2
# import os
from cvzone.FPS import FPS
fpsReader = FPS()
# color = ColorFinder()
cap = cv2.VideoCapture(0)
wCap = 1280
hCap = 720
fps = fpsReader.update()
# cv2.resize(cap, (1280, 720))
Taskbar = cv2.imread(r"C:\Users\xyz\PycharmProjects\PythonTuts\Python_other_tuts\murtaza_workshop\Projects\Resources\Taskbar.png")
# Taskbar = cv2.resize(Taskbar, (640, 125))
detector = HandDetector(detectionCon=0.85)
# cf = ColorFinder()

colors = [(255, 255, 255), (255, 0, 255),  (175, 125, 0), (175, 175, 0), (0, 0, 0)]
color = colors[0]
blank = cv2.FILLED
BrushThickNess = 30
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = cv2.resize(img, (1280, 720))
    # find hands
    hands, img = detector.findHands(img, flipType=False)
    if hands:
        hand1 = hands[0]
        lmList = hand1["lmList"]  # 21 landmarks
        bbox1 = hand1["bbox"]  # Bounding Box info x,y,,n
        if len(lmList) != 0:
            xp, yp = 0, 0
            x1, y1 = lmList[8][0], lmList[8][1]  # index finger tip
            x2, y2 = lmList[12][0], lmList[12][1]  # middle finger tip

            # find fingers up or not
            fingers = detector.fingersUp(hand1)
            # print(fingers)

            # drawing mode
            if fingers[1] != 0 and fingers[2] == 0:
                alll = cv2.circle(img, (x1, y1), 20, color, cv2.FILLED)
                # print("Drawing mode")
                if xp == 0 and yp == 0:
                    xp, yp = x1, y1
                if color == colors[4]:
                    cv2.line(img, (xp, yp), (x1, y1), color, 50)
                    cv2.line(imgCanvas, (xp, yp), (x1, y1), color, 50)
                    cv2.circle(img, (x1, y1), 8, (255, 255, 255), 5)

                else:
                    cv2.line(img, (xp, yp), (x1, y1), color, BrushThickNess)
                    cv2.line(imgCanvas, (xp, yp), (x1, y1), color, BrushThickNess)
                xp, yp = x1, y1

            # selection mode
            elif fingers[1] != 0 and fingers[2] == 1:
                # cv2.circle(img, (x2-30, y2), 20, (255, 0, 255), cv2.FILLED)
                xp, yp = 0, 0
                cv2.rectangle(img, (x1, y1), (x2, y2), color, cv2.FILLED)
                if y1 < 125:
                    if 150 < x1 < 350:
                        color = colors[1]
                    elif 450 < x1 < 650:
                        color = colors[2]
                    elif 750 < x1 < 950:
                        color = colors[3]
                    elif 1050 < x1 < 1250:
                        color = colors[4]
                        # blank = 5
                # print("Selection mode")
    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 58, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)
    # print(lmList)
    img[0:125, 0:1280] = Taskbar
    # print(type(img2))
    # painter = stackImages([img, imgCanvas, imgInv, imgGray], 2, 0.5)
    cv2.imshow("Paint", img)
    # cv2.imshow("Canvas", imgCanvas)
    # cv2.imshow("Painter", painter)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # to get exit from the videos
        break