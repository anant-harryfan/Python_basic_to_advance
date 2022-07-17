import cv2
from numpy import interp
from cvzone.HandTrackingModule import HandDetector
from time import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
################## Variables ######################
detector = HandDetector(detectionCon=0.8, maxHands=2)
frameWidth = 680    # values to set width of the screen
frameHeight = 420    # values to set height of the screen
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
pTime = 0  # help to set fps
minVol = volRange[0]
maxVol = volRange[1]
cap = cv2.VideoCapture(0)
volBar = 400
volPercent = 0
vol = 0
###################################################


while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))  # to set height and width of the screen
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)  # to get hands and flipType is used to get accurate left nad right hand and it wil return img
    if hands:
        hand1 = hands[0]  # 1 hand
        LnList1 = hand1["lmList"]  # List of 21 Landmarks points
        bbox1 = hand1["bbox"]  # Bounding Box info
        # print(bbox1)
        if len(LnList1) != 0:
            # Tabh hi work kare jabh hath ek specific distance pe ho
            area = (bbox1[2] + bbox1[0]) * (bbox1[3]+bbox1[1])//100
            # print(area)
            if 1500 < area < 2500:
                x1, y1 = LnList1[4][0], LnList1[4][1]  # thumb tip
                x2, y2 = LnList1[8][0], LnList1[8][1]  # index finger tip
                x3, y3 = LnList1[12][0], LnList1[12][1]  # middle finger tip
                # print(f"Thumb = {x1, y1}, \nIndex finger = {x2, y2}")

                l, info, img = detector.findDistance(LnList1[4], LnList1[8], img)  # distance find karta
                l2, info2 = detector.findDistance(LnList1[8], LnList1[12])
                # print(l)
                # hand range = 20 - 150
                # vol range = -65 - 0
                # print(l2)
                if l2 > 50:  # agar middle finger or index finger ki duri isse zayada hai tahh ye karo
                    volBar = interp(l, [20, 200], [400, 160])  # volume bar on image
                    volPercent = interp(l, [20, 200], [0, 100])  # volume persentage
                    # print(l, vol)
                    if l < 20:  # (min volume) thumbh ki duri index finger se itni kam hai to ye karo
                        # to bring smoothness
                        smoothness = 2
                        volPercent = smoothness * round(volPercent/smoothness)
                        cv2.circle(img, (info[4], info[5]), 15, (100, 100, 100), cv2.FILLED)  # distance ke beech wale me color change kae deta
                    elif l > 200:  # (max volume) agar inki duri isse zayda hai to ye karo
                        cv2.circle(img, (info[0], info[1]), 15, (100, 100, 100), cv2.FILLED)  # index pe color change karta
                        cv2.circle(img, (info[2], info[3]), 15, (100, 100, 100), cv2.FILLED)  # middle pe color hange arta
                else:  # jabh middle finger uper ho jae
                    volume.SetMasterVolumeLevelScalar(volPercent/100, None)  # volume set kardo
                    cv2.putText(img, f"Volume set at {int(volPercent)}%", (130, 200), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 255), 5)  # kitni vol hai abhi hai vo display kar vao

    cVol = int(volume.GetMasterVolumeLevelScalar() * 100)  # current volume
    cv2.putText(img, f'Vol Set: {int (cVol)}', (400, 58), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)  # volume kitni hai corner pe batata
    cv2.rectangle(img, (58, 158), (85, 400), (1, 1, 1), 2)
    cv2.rectangle(img, (58, int(volBar)), (85, 400), (1, 1, 1), cv2.FILLED)
    cv2.putText(img, f"{int(volPercent)}%", (40, 150), cv2.FONT_HERSHEY_PLAIN, 3, (1, 1, 1), 3)

# FPS
    cTime = time()
    fps = 1 / (cTime - pTime) + 10
    pTime = cTime
    cv2.putText(img, f"{int(fps)}", (40, 70), cv2.FONT_HERSHEY_PLAIN, 3, (1, 1, 1), 3)
    cv2.imshow("video", img)  # to show video
    if cv2.waitKey(1) & 0xFF == ord('q'):  # to get exit from the videos
        break
cv2.waitKey(1)