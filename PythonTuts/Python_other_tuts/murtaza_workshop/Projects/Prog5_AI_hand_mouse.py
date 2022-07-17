import cv2
import numpy as np
from cvzone import HandTrackingModule
import time
from pynput.mouse import Button, Controller
# import pyautogui

################################## Variables #########################################
wCap = 600
hCap = 680
controller = HandTrackingModule.HandDetector(detectionCon=0.8)
cap = cv2.VideoCapture(0)
mouse = Controller()
# height, width = pyautogui.size()
# print(width, height)
frameR = 10
smoothing = 2
pLocX, pLocY = 0, 0
cLocX, cLocY = 0, 0
######################################################################################

cap.set(3, wCap)
cap.set(4, hCap)
while True:
    ################# Read Image ###################
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hand, img = controller.findHands(img, flipType=False)
    ################################################
    cv2.rectangle(img, (frameR, frameR), (wCap, hCap - 400), (1, 1, 1), 5)

# detect hand is there or not
    if hand:
        # if True so hand1 = that hand
        hand1 = hand[0]
        # lmlist
        lmList1 = hand1["lmList"]
        # bbox
        bbox1 = hand1["bbox"]
        # print(bbox1)

        if len(lmList1) != 0:
            # index finger
            x1, y1 = lmList1[8][0:]
            # middle finger
            x2, y2 = lmList1[12][0:]
            # print(x1, y1)
            # print(x2, y2)
            # tell that fingers ar eup or not
            fingers = controller.fingersUp(hand1)
            # print(fingers)
            # print(l)
            # bas index finger uper ho tabh ye karo
            if fingers[1] == 1 and fingers[2] == 0:
                # jo box ka sie hai usse pure screen ka sie banado
                x3 = np.interp(x1, (frameR, wCap - 50), (0, 1350.0))
                y3 = np.interp(y1, (frameR, hCap - 200), (0, 1400.0))
                # print(x3, y3)
                # smooth karna hai agar cursor ko to ye kam aaya hai
                cLocX = pLocX + (x3-pLocX) / smoothing
                cLocY = pLocY + (y3-pLocY) / smoothing
                # print("c", cLocX, cLocY)
                # print("p", pLocX, pLocY)
                # ungli ki podtiton se cursor ko hilata
                mouse.position = (cLocX, cLocY)
                # ungli pe circle
                cv2.circle(img, (x1, y1), 15, (1, 1, 1), cv2.FILLED)
                pLocX, pLocY = cLocX, cLocY
                # agar index and middle finger dono uper hai
            elif fingers[1] == 1 and fingers[2] == 1:
                # distance find karta
                l, info, img = controller.findDistance(lmList1[8], lmList1[12], img)
                # click karna
                if l < 22:
                    mouse.click(Button.left, 1)
                    cv2.circle(img, (info[4], info[5]), 15, (100, 100, 100), cv2.FILLED)

    # show video
    cv2.imshow("mouse", img)
    # q dabane pe exit
    if cv2.waitKey(1) & 0xFF == ord('q'):   # to get exit from the videos
        break
cv2.waitKey(1)