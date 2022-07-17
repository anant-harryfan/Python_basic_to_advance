import cv2
from cvzone.HandTrackingModule import HandDetector
from math import sqrt
from numpy import polyfit
from cvzone.Utils import putTextRect

def findScreenDis(x, y):
    x3 = [435, 410, 372, 334, 300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]

    y3 = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95,
         100]  # before 20 its not real a measurement in cm but after 20 it is in o real measurement
    coff = polyfit(x3, y3, 2)  # y = Ax^2 + Bx + C
    distance = int(sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2))  # to find from the screen
    A, B, C = coff
    distanceCM = A * distance ** 2 + B * distance + C
    # print(int(distanceCM), distance)
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)
    putTextRect(img, f'{int(distanceCM)} cm', (x + 5, y - 10))

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
# Find Function
# x is the raw distance y is the value in cm
# coff = polyfit(x, y, 2)  # y = Ax^2 + Bx + C
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1380, 720))
    img = cv2.flip(img, 1)
    hands= detector.findHands(img, flipType=False, draw=False)
    if hands:
        hand1 = hands[0]
        lmList = hand1["lmList"]
        x, y, w, h = hand1["bbox"]
        x1, y1 = lmList[5]
        x2, y2 = lmList[17]
        # distance = int(sqrt((y2 - y1)**2 + (x2-x1)**2))   # to find from the screen
        # A, B, C = coff
        # distanceCM = A * distance ** 2 + B * distance + C
        # # print(int(distanceCM), distance)
        # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)
        # putTextRect(img, f'{int(distanceCM)} cm', (x + 5, y - 10))
    cv2.imshow("Ram", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # to get exit from the videos
        break