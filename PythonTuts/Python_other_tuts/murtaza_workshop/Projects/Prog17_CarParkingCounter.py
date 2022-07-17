import cv2
import pickle
import cvzone
import numpy as np
path = "Resources/Prog17_CarParkProject/carPark.mp4"
cap = cv2.VideoCapture(path)
width, height = 107, 48

with open("Resources/Prog17_CarParkProject/CarParkPos", "rb") as f:
    posList = pickle.load(f)

# stakuImg = []
def checkParkingSpaces(ImgPre):
    spaceCounter = 0
    for pos in posList:
        x, y = pos
        imgCrop = ImgPre[y:y+height, x:x+width]
        # stakuImg.append(imgCrop)
        count = cv2.countNonZero(imgCrop)
        if count<900:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 2
        cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), color, thickness)
        cvzone.putTextRect(img, str(count), (x, y+height-5), scale=1, thickness=2, offset=0, colorR=color)

    cvzone.putTextRect(img, f"Free: {spaceCounter}/{len(posList)}", (100, 60), scale=5, thickness=5, offset=10, colorR=(0, 200, 0))


while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_MSEC, 0)

    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernal = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernal, iterations=1)

    checkParkingSpaces(imgDilate)
    # to show all box
    # stacka = cvzone.stackImages(stakuImg, 300, 0.1)
    # for pos in posList:
        # cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), (255, 0, 0), 4)
        # cv2.imshow("Krishna", stacka)


    RamKrishnaHari = cvzone.stackImages([img, imgGray, imgBlur, imgThreshold, imgMedian, imgDilate], 2, 0.3)
    cv2.imshow("RamKrishnaHari", RamKrishnaHari)
    cv2.imshow("Hari", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # to get exit from the videos
        break