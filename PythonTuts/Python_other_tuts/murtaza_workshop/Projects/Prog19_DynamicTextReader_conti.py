import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.Utils import putTextRect, stackImages
import numpy as np

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)
# TextList = ["Welcome to", "anant chandak", "Here we will Talk about", "krishna", "Jagannath", "Jay shree ram", "keshav", "Madhav"]
TextList = ["Welcome to", "Anant chandak", "Here we will Talk about", "Robot", "Open-cv", "python"]
while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)
    imgText = np.zeros_like(img)

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]

        w, _ = detector.findDistance(pointLeft, pointRight)
        W = 6.3

        # Finding distance
        f = 840
        d = (W * f) / w
        # print(d)

        putTextRect(img, f'Depth: {int(d)}cm',
                           (face[10][0] - 100, face[10][1] - 50),
                           scale=2)

        for i, text in enumerate(TextList):
            smoothNess = (int(d / 20) * 20)
            singleHeight = 20 + int(smoothNess/4)
            scale = 0.4 + smoothNess / 75
            cv2.putText(imgText, text, (50, 50+(i*singleHeight)), cv2.FONT_ITALIC, scale, (255, 255, 255), 2)

    imgStacked = stackImages([img, imgText],  2, 1)
    cv2.imshow("RamKrishna", imgStacked)
    cv2.waitKey(1)