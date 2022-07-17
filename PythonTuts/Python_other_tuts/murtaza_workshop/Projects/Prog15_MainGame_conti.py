import cv2
from cvzone.HandTrackingModule import HandDetector
from math import sqrt
from numpy import polyfit
from cvzone.Utils import putTextRect
from random import randint
from time import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
# Find Function
# x is the raw distance y is the value in cm
x = [435, 410, 372, 334, 300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
y = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]  # before 20 its not real a measurement in cm but after 20 it is in o real measurement
coff = polyfit(x, y, 2)  # y = Ax^2 + Bx + C

# Game Variables
cx, cy = 250, 250
color = (255, 0, 0)
counter = 0
score = 0
timeStart = time()
totalTime = 30
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1380, 720))
    img = cv2.flip(img, 1)
    if time() - timeStart < totalTime:

        hands = detector.findHands(img, flipType=False, draw=False)
        if hands:
            hand1 = hands[0]
            lmList = hand1["lmList"]
            x, y, w, h = hand1["bbox"]
            x1, y1 = lmList[5]
            x2, y2 = lmList[17]
            distance = int(sqrt((y2 - y1)**2 + (x2-x1)**2))   # to find from the screen
            A, B, C = coff
            distanceCM = A * distance ** 2 + B * distance + C

            if distanceCM < 20:
                counter = 1


            cv2.rectangle(img, (x - 30, y - 30), (x + w + 30, y + h + 30), (0, 0, 0), 3)
            putTextRect(img, f'{int(distanceCM)} cm', (x + 5, y - 10))
        if counter:
            counter += 1
            color = (0, 255, 0)
            if counter == 5:
                cx, cy = randint(100, 1100), randint(100, 600)
                color = (255, 0, 0)
                score += 1
                counter = 0
        # Draw Target
        cv2.circle(img, (cx, cy), 30, color, cv2.FILLED)
        cv2.circle(img, (cx, cy), 10, (255, 255, 255), cv2.FILLED)
        cv2.circle(img, (cx, cy), 20, (255, 255, 255), 2)
        cv2.circle(img, (cx, cy), 30, (50, 50, 50), 2)

        # Game Graphics
        img, bbox = putTextRect(img, f"Time: {int(totalTime - (time() - timeStart))}", (1100, 75), scale=3, offset=30)
        img, bbox2 = putTextRect(img, f"Score: {str(score).zfill(2)}", (60, 75), scale=3, offset=30)
    else:
        putTextRect(img, 'Game Over', (400, 400), scale=5, offset=30, thickness=7)
        putTextRect(img, f'Your Score: {score}', (450, 500), scale=3, offset=20)
        putTextRect(img, 'Press R to restart', (460, 575), scale=2, offset=10)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    if key == ord('r'):
        timeStart = time()
        score = 0
