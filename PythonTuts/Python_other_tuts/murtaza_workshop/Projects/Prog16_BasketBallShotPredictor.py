import cv2
from cvzone.ColorModule import ColorFinder
from cvzone.Utils import findContours, putTextRect, stackImages
from numpy import polyfit
import math

path = "Resources/Prog16_files/vid (4).mp4"
pathImg = "Resources/Prog16_files/ball.png"
cap = cv2.VideoCapture(path)
detector = ColorFinder(False)
frameCounter = 0
# {'hmin': 0, 'smin': 143, 'vmin': 0, 'hmax': 123, 'smax': 255, 'vmax': 237}  # totally remove ackground bt some part of bal is cut (Recommended)
# {'hmin': 0, 'smin': 114, 'vmin': 0, 'hmax': 96, 'smax': 255, 'vmax': 255}  # remain total ball but background is not fully cut

hsv = {'hmin': 0, 'smin': 143, 'vmin': 0, 'hmax': 123, 'smax': 255, 'vmax': 237}

PosListX, PosListY = [], []
xList = [item for item in range(0, 1300)]

while True:
    frameCounter += 1
    # HELPS TO REPLAY VIDEO WHEN IT END
    if frameCounter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        frameCounter = 0
        PosListX, PosListY = [], []
        cap.set(cv2.CAP_PROP_POS_MSEC, 0)
    success, img = cap.read()
    # img = cv2.imread(pathImg)
    img = cv2.resize(img, (0, 0), None, 0.7, 0.7)
    # img = cv2.flip(img, 1)
    img2 = img[0:460, :]

    # finding color of ball
    imgColor, mask = detector.update(img2, hsv)
    # finding position of ball
    imgContours, contours = findContours(img2, mask, minArea=200)
    imgResult = img2.copy()
    if contours:
        PosListX.append(contours[0]["center"][0])
        PosListY.append(contours[0]["center"][1])

    if PosListX:
        # Prediction by Polynomial Regression y = Ax^2 + Bx + C
        # finding Coefficients
        A, B, C = polyfit(PosListX, PosListY, 2)
        for i, (posx, posy) in enumerate(zip(PosListX, PosListY)):
            pos = (posx, posy)
            if i == 0:
                cv2.line(imgResult, pos, pos, (0, 255, 0), 5)
            else:
                cv2.line(imgResult, pos, (PosListX[i-1], PosListY[i-1]), (0, 255, 0), 7)
            cv2.circle(imgResult, pos, 5, (0, 0, 0), cv2.FILLED)
        for x in xList:
            y = int(A*x**2 + B*x + C)
            cv2.circle(imgResult, (x, y), 2, (255, 0, 0), cv2.FILLED)

        if len(PosListX) < 10:
            # Prediction
            # X values 330 to 430  Y 590
            a = A
            b = B
            c = C - 400

            x = int((-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
            prediction = 230 < x < 300
            cv2.line(imgResult, (230, 400), (300, 400), (0, 0, 0), 20)

        if prediction:
            putTextRect(imgResult, "Basket", (50, 150),
                               scale=5, thickness=5, colorR=(0, 200, 0), offset=20)
        else:
            putTextRect(imgResult, "No Basket", (50, 150),
                               scale=5, thickness=5, colorR=(0, 0, 200), offset=20)

    img = cv2.resize(img, (910, 460))
    # print(img2.shape[0], img2.shape[1])
    imgStack = stackImages([img2, imgColor, mask, imgContours, imgResult, img], 2, 0.5)
    # cv2.imshow("Ram", img)
    # cv2.imshow("Ram", imgColor)
    cv2.imshow("RamKrishnaHari", imgStack)

    if cv2.waitKey(50) & 0xFF == ord('q'):  # to get exit from the videos
        break