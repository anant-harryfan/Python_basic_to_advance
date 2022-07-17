import cv2
from cvzone.Utils import findContours, stackImages, cornerRect
import numpy as np


Question = 5
choices = 5
ans = [0, 1, 0, 1, 3]
color = (0, 255, 0)

def splitBoxes(img):
    rows = np.vsplit(img, 5)
    boxes = []
    for r in rows:
        cols = np.hsplit(r, 5)
        for i, box in enumerate(cols):
            boxes.append(box)
    # ram = stackImages(boxes, 3, 1)
    # cv2.imshow(f"ram", ram)
    return boxes

def showAns(img, myIndex, grading, ans2, question, choices):
    secW = int(img.shape[1]/Question)
    secH = int(img.shape[0]/choices)
    for x in range(0, question):
        myAns = myIndex[x]
        cx = (myAns*secW)+secW//2
        cy = (x*secH) + secH//2
        if grading[x] == 1:
            color = (0, 255, 0)
        else:
            color = (0, 0, 255)
            correctAns = ans[x]
            cv2.circle(img, ((correctAns*secW)+secW//2, (x*secH-20)+secH//2), 15, (0, 255, 0), cv2.FILLED)
        cv2.circle(img, (cx, cy-10), 25, color, cv2.FILLED)
    return img

# cap = cv2.VideoCapture(0)

while True:
    # success, img = cap.read()
    img = cv2.imread("Resources/Prog22_OMR.png")
    # img = cv2.resize(img, (1380, 720))
    # img = cv2.flip(img, 1)
    # Preprocess
    img = cv2.detailEnhance(img, sigma_s=10, sigma_r=0.5)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
    imgCanny = cv2.Canny(imgBlur, 10, 50)
    imgDilate = cv2.dilate(imgCanny, (7, 7), iterations=1)
    imgContours, confound = findContours(img, imgDilate, filter=4, minArea=1000)
    BiggestBbox = confound[0]["bbox"]
    BiggestBbox2nd = confound[1]["bbox"]
    # print(BiggestBbox)

    # wrap = Bird(BiggestBbox, img)
    x, y, w, h = BiggestBbox
    x1, y1 = x + w, y + h
    width, height = 200, 100

    pts1 = np.float32([[x, y], [x1, y], [x, y1], [x1, y1]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgWrapCol = cv2.warpPerspective(img, matrix, (200, 100))
    imgWrapCol = cv2.resize(imgWrapCol, (300, 400))
    # apply threshold
    imgWrapGray = cv2.cvtColor(imgWrapCol, cv2.COLOR_BGR2GRAY)
    imgThresh = cv2.threshold(imgWrapGray, 150, 255, cv2.THRESH_BINARY_INV)[1]
    boxes = splitBoxes(imgThresh)
    # non zero pixel val
    myPixelVal = np.zeros((Question, choices))
    countC, countR = 0, 0
    for image in boxes:
        totalPixels = cv2.countNonZero(image)
        myPixelVal[countR][countC] = totalPixels
        countC += 1
        if countC == choices:
            countR += 1
            countC = 0
    # print(myPixelVal)
    # finding index val of markings
    myIndex = []
    for x in range(0, Question):
        arr = myPixelVal[x]
        myIndexVal = np.where(arr == np.amax(arr))
        # print(myIndexVal[0])
        # print(arr)
        myIndex.append(myIndexVal[0][0])
    # print("myIndex", myIndex)
   # grading
    grading = []
    for i in range(0, Question):
        if ans[i] == myIndex[i]:
            grading.append(1)
        elif ans[i] != myIndex[i]:
            grading.append(0)
    # print("ans", ans)
    # print("grading", grading)

    # Score
    score = (sum(grading)/Question) * 100
    # print(score)

    # Putting text
    cx, cy = confound[1]["center"]
    cv2.putText(img, f"{score}", (cx-20, cy+5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)

    # showing ans
    imgResult = imgWrapCol.copy()
    imgResult = showAns(imgResult, myIndex, grading, ans, Question, choices)
    imgDrawings = np.zeros_like(imgWrapCol)
    imgDrawings = showAns(imgDrawings, myIndex, grading, ans, Question, choices)
    imgDrawings = cv2.resize(imgDrawings, (200, 100))
    invmatrix = cv2.getPerspectiveTransform(pts2, pts1)
    imgInvWrap = cv2.warpPerspective(imgDrawings, invmatrix, (250, 261))
    imgFinal = img.copy()
    # print(img.shape)
    imgFinal = cv2.addWeighted(imgFinal, 1, imgInvWrap, 20, 0)
    imgFinal = cv2.resize(imgFinal,  (361, 350))


    img = cornerRect(img, BiggestBbox, l=10, t=2, rt=0)
    img = cornerRect(img, BiggestBbox2nd, l=10, t=2, rt=0, colorC=(0, 0, 255))
    RamKrishnaHari = stackImages([img, imgGray, imgBlur, imgCanny, imgDilate, imgContours], 4, 1)
    BhramaVishnuMahesh = stackImages([imgWrapCol, imgWrapGray, imgThresh], 4, 1)
    cv2.imshow("madhav", imgDrawings)
    cv2.imshow("keshav", imgFinal)
    cv2.imshow("BhramaVishnuMahesh", BhramaVishnuMahesh)
    cv2.imshow("RamKrishnaHari", RamKrishnaHari)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # to get exit from the videos
        break
