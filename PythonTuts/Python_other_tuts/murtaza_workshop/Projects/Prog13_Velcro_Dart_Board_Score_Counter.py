import cv2
import cvzone
import numpy as np
import pickle

path = "Resources/Prog13_Videos/Video2.mp4"
cap = cv2.VideoCapture(path)
frameCounter = 0
cornerPoints = [[377, 52], [944, 71], [261, 624], [1058, 612]]
colorFinder = cvzone.ColorFinder(False)
hsvValues = {'hmin': 32, 'smin': 99, 'vmin': 88, 'hmax': 49, 'smax': 255, 'vmax': 255}
countHit = 0
imgListBallsDetected = []
hitDrawBallInfoList = []
totalScore = 0

with open("Prog13_Poly_points", 'rb') as f:
    polygonWithScore = pickle.load(f)
print(polygonWithScore)
# to get Wrap perspective of bord
def getBoard(img):
    width, height = int(400 * 1.5), int(300 * 1.5)
    pts1 = np.float32(cornerPoints)
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (width, height))
    for i in range(4):
        cv2.circle(img, (cornerPoints[i][0], cornerPoints[i][1]), 15, (0, 0, 0), cv2.FILLED)
    return imgOutput
# detect darts
def detectColorDarts(img):
    imgBlur = cv2.GaussianBlur(img, (7, 7), 2)
    imgColor, mask = colorFinder.update(imgBlur, hsvValues)
    kernal = np.ones((9, 9), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

    # kernal = np.ones((11, 11), np.uint8)
    mask = cv2.dilate(mask, kernal, iterations=3)

    # mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
    return imgColor, mask
while True:
    # .SET() WILL WORK IN WHILE LOOP
    cap.set(3, 1380)
    cap.set(4, 720)
    frameCounter += 1
    # HELPS TO REPLAY VIDEO WHEN IT END
    if frameCounter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        frameCounter = 0
        totalScore = 0 - 60
        cap.set(cv2.CAP_PROP_POS_MSEC, 0)
    success, img = cap.read()
    # img = cv2.imread("0.Resources_GameDev/Prog13_Videos/img.png")
    # tells the mask
    # imgColor, mask = colorFinder.update(img, hsvValues)
    imgBoard = getBoard(img)
    imgColor, mask = detectColorDarts(imgBoard)
    # Remove previous detection
    for i, img in enumerate(imgListBallsDetected):
        mask = mask - img
        # cv2.imshow(str(i), img)
    imgContour, ContourFound = cvzone.findContours(imgBoard, mask, 3500)
     # tells hit detected
    if ContourFound:
        countHit += 1
        # we do this because we don't want that a ball cames in a image and fall down as a hit
        if ContourFound:
            countHit += 1
            if countHit == 20:
                imgListBallsDetected.append(mask)
                # print("Hit Detected")
                countHit = 0
                for polyScore in polygonWithScore:
                    center = ContourFound[0]['center']
                    poly = np.array([polyScore[0]], np.int32)
                    inside = cv2.pointPolygonTest(poly, center, False)
                    # print(inside)
                    if inside == 1:
                        # print("Yes")
                        hitDrawBallInfoList.append([ContourFound[0]['bbox'], ContourFound[0]['center'], poly])
                        totalScore += polyScore[1]
        print(totalScore)
    imgBlank = np.zeros((imgContour.shape[0], imgContour.shape[1], 3), np.uint8)
    for bbox, center, poly in hitDrawBallInfoList:
        cv2.rectangle(imgContour, bbox, (0, 0, 0), 2)
        cv2.circle(imgContour, center, 5, (255, 255, 255), cv2.FILLED)
        cv2.drawContours(imgBlank, poly, -1, color=(0, 255, 0), thickness=cv2.FILLED)

    imgBoard = cv2.addWeighted(imgBoard, 0.7, imgBlank, 0.5, 0)
    imgBoard, _ = cvzone.putTextRect(imgBoard, f'Total Score: {totalScore}',                                     (10, 40), scale=2, offset=20)

    # cv2.imwrite("0.Resources_GameDev/Prog13_Videos/imgBoard.png", imgBoard)
    imgStacked = cvzone.stackImages([imgContour, imgColor, mask, imgBoard], 2, 0.5)
    cv2.imshow("RamKrishnaMadhav", imgStacked)
    # cv2.imshow("Krishna", imgContour)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # to get exit from the videos
        break