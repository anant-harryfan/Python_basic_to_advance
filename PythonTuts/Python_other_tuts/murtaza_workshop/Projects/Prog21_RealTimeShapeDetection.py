import cv2
from cvzone import stackImages
from cvzone import findContours
import numpy as np

def empty(a):
    pass

cv2.namedWindow("Hanuman")
cv2.resizeWindow("Hanuman", 640, 240)
cv2.createTrackbar("Threshold1", "Hanuman", 22, 255, empty)
cv2.createTrackbar("Threshold2", "Hanuman", 51, 255, empty)
cv2.createTrackbar("Area", "Hanuman", 5000, 30000, empty)

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    img = cv2.resize(img, (300, 220))
    img = cv2.flip(img, 1)
    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    threshold1 = cv2.getTrackbarPos('Threshold1', "Hanuman")
    threshold2 = cv2.getTrackbarPos('Threshold2', "Hanuman")
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    kernal = np.array((7, 7))
    imgDilate = cv2.dilate(imgCanny, kernal, iterations=1)
    areaMin = cv2.getTrackbarPos("Area", "Hanuman")
    imgContour, Contours = findContours(img, imgDilate, minArea=areaMin)
    if Contours:
        cnt = Contours[0]["cnt"]
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        x, y, w, h = Contours[0]["bbox"]
        cv2.putText(imgContour, "Points: " + f"{len(approx)} ", (x + w + 20, y + 20), cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 255, 0), 2)
        cv2.putText(imgContour, "Area: " + f"{int(Contours[0]['area'])} ", (x + w + 20, y + 45), cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 255, 0), 2)

    ramKrishnaHari = stackImages([img, imgBlur, imgGray, imgCanny, imgContour], 2, 1)
    cv2.imshow("RamKrishnaHari", ramKrishnaHari)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # to get exit from the videos
        break