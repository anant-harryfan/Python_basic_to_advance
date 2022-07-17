import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import os
################## Variables ######################
detector = HandDetector(detectionCon=0.8, maxHands=2)
frameWidth = 700    # values to set width of the screen
frameHeight = 500    # values to set height of the screen
path = r"C:\Users\xyz\PycharmProjects\PythonTuts\Python_other_tuts\murtaza_workshop\Projects\Resources\Prog2_images"
myList = os.listdir(path)
# print(myList)
overlayList = []
cap = cv2.VideoCapture(0)
###################################################
for imPath in myList:
    image = cv2.imread(f"{path}/{imPath}")
    imgResize = cv2.resize(image, (200, 200))
    # print(f"{path}/{imPath}")
    overlayList.append(imgResize)
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1380, 720))  # to set height and width of the screen
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)  # to get hands and flipType is used to get accurate
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        fingers = detector.fingersUp(hand1)
        FingersUp = fingers.count(1)
        img[0:200, 0:200] = overlayList[FingersUp-1]
        cv2.rectangle(img, (20, 225), (170, 425), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, str(FingersUp), (55, 375), cv2.FONT_HERSHEY_PLAIN, 8, (255, 255, 255), 9)
        # print(fingers)
    cv2.imshow("video", img)  # to show video
    if cv2.waitKey(1) & 0xFF == ord('q'):  # to get exit from the videos
        break
