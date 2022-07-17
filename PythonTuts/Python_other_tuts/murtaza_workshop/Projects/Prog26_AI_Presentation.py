import os
import numpy as np
import cv2
from cvzone.HandTrackingModule import HandDetector

# video
cap = cv2.VideoCapture(0)
# hand detector
detector = HandDetector()

# list of img in ppt
# we have one sorted to bring 2 digit number (after 10) at last
folderPath = "Resources/Prog26_ppt"
ListImg = sorted(os.listdir(folderPath), key=len)
# print(ListImg)

imgNumber = 0

# height of small img (video img)
hs, ws = int(120 * 2), int(213 * 2)  # width and height of small image
# threshold
gesThresh = 300
lol = 450
# to give some pause when we use our finger to move from one slide to another
buttonPress = False
buttonDelay = 10
counter = 0
width, height = 1280, 720
# drawing ke liye
annotation = [[]]
annotationNumber = 0
annotationStart = False

while True:
    # img
    _, img = cap.read()
    img = cv2.resize(img, (width, height))
    img = cv2.flip(img, 1)
    pathImg = os.path.join(folderPath, ListImg[imgNumber])
    imgCurrent = cv2.imread(pathImg)
    imgCurrent = cv2.resize(imgCurrent, (width, height))

    # cv2.rectangle(imgCurrent, (0, 0), (width, height), (0, 0, 0), cv2.FILLED)
    hands, img = detector.findHands(img, flipType=False)
    cv2.line(img, (0, gesThresh), (width, gesThresh), (255, 255, 0), 10)
    # buttonpress isliye kiya taki ek hi ba me bhhot sari slide change na karde jabh ham thubh ya piny finger use kare
    if hands and buttonPress == False:
        hand1 = hands[0]
        lmList = hand1["lmList"]
        cx, cy = hand1["center"]
        finger = detector.fingersUp(hand1)
        # ek specific jagha se pure screen ko access karle pointer se
        xVal = int(np.interp(lmList[8][0], [width // 2, width-50], [0, width]))
        yVal = int(np.interp(lmList[8][1], [150, height - 250], [0, height]))

        indexFinger = xVal, yVal
        # indexFinger = lmList[8][0], lmList[8][1]
        # print(finger)
        # kabhi galti se comp hath ko detect karke khurafati na machae to face ke uper hath aayega tabh kuch karo
        if cy <= gesThresh:
            # Gesture1 - thubh se piche slide pe or pinky se agge wali slide pe janna
            if finger == [1, 0, 0, 0, 0]:
                if imgNumber > 0:
                    imgNumber = imgNumber-1
                    annotation = [[]]
                    annotationNumber = 0
                    annotationStart = False
                    buttonPress = True

            elif finger == [0, 0, 0, 0, 1]:
                if imgNumber < len(ListImg)-1:
                    imgNumber = imgNumber+1
                    annotation = [[]]
                    annotationNumber = 0
                    annotationStart = False
                    buttonPress = True


        # Gesture2 - Pointer
        elif finger == [0, 1, 1, 0, 0]:
            # print(indexFinger)
            cv2.circle(imgCurrent, indexFinger, 15, (0, 0, 200), cv2.FILLED)
            annotationStart = False


        # Gesture3 - painter
        if finger == [0, 1, 0, 0, 0]:
            if annotationStart is False:
                annotationStart = True
                annotationNumber += 1
                annotation.append([])
            cv2.circle(imgCurrent, indexFinger, 15, (0, 0, 255), cv2.FILLED)
            # jabh ye ho to annotation me append kardo
            annotation[annotationNumber].append(indexFinger)
        else:
            annotationStart = False
        # Gesture 4 - undo or eraser
        if finger == [0, 1, 1, 1, 0]:
            if annotation:
                annotation.pop(-1)
                annotationNumber -= 1
                buttonPressed = True
                print(buttonPressed)
                annotationStart = False

    else:
        annotationStart = False

# ki agar next slide pe gae to buttondelay(10 frames) ruko phir agge jana
    if buttonPress:
        counter += 1
        if counter > buttonDelay:
           counter = 0
           buttonPress = False

    # draw kardo matlab previus index finger ki location se abhi ki location tak
    for i in range(len(annotation)):
        for j in range(len(annotation[i])):
            if j != 0:
                cv2.line(imgCurrent, annotation[i][j - 1], annotation[i][j], (0, 0, 255), 12)
    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w - ws: w] = imgSmall
    cv2.imshow("Ram", img)
    cv2.imshow("krishna", imgCurrent)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # to get exit from the videos
        break
