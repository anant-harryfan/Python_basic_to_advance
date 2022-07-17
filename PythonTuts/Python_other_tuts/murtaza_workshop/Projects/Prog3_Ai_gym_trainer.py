from cvzone.PoseModule import PoseDetector as pd
import cv2
import numpy as np

detector = pd()
videoPath = r"C:\Users\xyz\PycharmProjects\PythonTuts\Python_other_tuts\murtaza_workshop\Projects\Resources\Prog3\1.mp4"
cap = cv2.VideoCapture(videoPath)
path = r"Resources/Prog3\testu.jpg"
count = 0
dire = 0
while True:
    success, img = cap.read()

    # img = cv2.imread(path)
    img = cv2.resize(img, (1280, 728))
    img = detector.findPose(img, False)

    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:

        angle = detector.findAngle(img, 11, 13, 15, draw=False)
        per = np.interp(angle, (210, 310), (0, 100))
        bar = np.interp(angle, (210, 310), (650, 100))
        color = (255, 0, 255)
        if per == 100:
            color = (255, 255, 0)
            if dire == 0:
                count += 0.5
                dire = 1
        if per == 0:
            color = (255, 255, 0)
            if dire == 1:
                count += 0.5
                dire = 0

        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f"{int(per)}%", (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4, color, 4)
        cv2.rectangle(img, (0, 450), (250, 720), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15, (255, 255, 255), 25)

    cv2.imshow("Image", img)
    cv2.waitKey(1)