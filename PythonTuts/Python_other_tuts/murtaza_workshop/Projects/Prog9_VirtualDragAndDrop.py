import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.Utils import cornerRect
import numpy as np

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.3, maxHands=1)
colorR = (255, 0, 255)
cx, cy, w, h = 100, 100, 200, 200

class DragRect():
    def __init__(self, posCenter, size=[200, 200]):
        self.posCenter = posCenter
        self.size = size

    def update(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size

        if cx - w // 2 < cursor[0] < cx + w // 2 and cy - h // 2 < cursor[1] < cy + h // 2:
            colorR = (255, 255, 0)
            self.posCenter = cursor
RectList = []
for i in range(5):
    RectList.append(DragRect([i*250+150, 150]))

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)
    if hands:
        hand1 = hands[0]  # 1 hand
        lmList = hand1["lmList"]  # List of 21 Landnarks points
        bbox = hand1["bbox"]  # Bounding Box info x,y,n
        if lmList:
            l, info = detector.findDistance(lmList[8], lmList[12])
            # print(l)
            if l < 100:
                cursor = lmList[8]
                for rect in RectList:
                    rect.update(cursor)

            else:
                colorR = (255, 0, 255)
    for rect in RectList:
        cx, cy = rect.posCenter
        w, h = rect.size
        cv2.rectangle(img, (cx-w//2, cy-h//2), (cx+w//2, cy+h//2), colorR, cv2.FILLED)
        # cornerRect(img, (cx-w//2, cy-h//2, cx+w//2, cy+h//2, w, h), 20, 4)
    cv2.imshow("img", img)
    cv2.waitKey(1)
