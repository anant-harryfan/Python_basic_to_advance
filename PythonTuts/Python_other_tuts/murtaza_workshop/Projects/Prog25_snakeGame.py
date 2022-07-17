import math
import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
from cvzone import overlayPNG
import numpy as np

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)
class SnakeGame:
    def __init__(self, pathFood):
        self.points = []  # all points of snake
        self.lengths = []  # distance between each point
        self.currentLength = 0  # total length of snake
        self.allowedLength = 150  # length of snake body
        self.previousHead = 0, 0  # previous head point
        self.food = cv2.imread(pathFood, cv2.IMREAD_UNCHANGED)  # food image
        self.hFood, self.wFood, _ = self.food.shape  # getting width and height
        self.foodPoint = 0, 0   # food point
        # to get random location of food
        self.randomLocation()
        # score
        self.score = 0
        # game over
        self.gameOver = False

    def randomLocation(self):
        """set random location"""
        self.foodPoint = random.randint(100, 1000), random.randint(100, 500)

    def update(self, imgMain, currentHead):
        """update snake"""

        if self.gameOver:
            cvzone.putTextRect(imgMain, "Game Over", [300, 400],
                               scale=7, thickness=5, offset=20)
            cvzone.putTextRect(imgMain, f'Your Score: {self.score}', [300, 550],
                               scale=7, thickness=5, offset=20)

        else:
            # previous location
            px, py = self.previousHead
            # current location
            cx, cy = currentHead
            # add kar rahe current pos ko
            self.points.append([cx, cy])
            # distance find kar rahe zayada achhe tarike se
            distance = math.hypot(cx-px, cy-py)
            # length me append kar rahe
            self.lengths.append(distance)
            # current snake ke length ko distance se plus kar rahe
            self.currentLength += distance
            # phir previous pos ko current pos bana rahe
            self.previousHead = cx, cy

            # Length reduction
            # agar snake apni aukat se bahar jae to cat do
            if self.currentLength > self.allowedLength:
                for i, length in enumerate(self.lengths):
                    self.currentLength -= length
                    self.lengths.pop(i)
                    self.points.pop(i)
                    # jabh aukat me aajae tabh all is well
                    if self.currentLength < self.allowedLength:
                        break

            # Check if snake ate the food
            rx, ry = self.foodPoint
            if rx - self.wFood//2 < cx < rx+self.wFood//2 and ry - self.wFood//2 < cy < ry+self.hFood//2:
                self.randomLocation()
                self.allowedLength += 50
                self.score += 1
                print(self.score)

            # Draw snake
            if self.points:
                for i, point in enumerate(self.points):
                    if i != 0:
                        cv2.line(imgMain, self.points[i-1], self.points[i], (0, 0, 255), 20)
                cv2.circle(imgMain, self.points[-1], 4, (0, 0, 0), 20)

            # Draw food
            rx, ry = self.foodPoint
            imgMain = overlayPNG(imgMain, self.food, (rx-self.wFood//2, ry-self.hFood//2))

            # Check collision
            pts = np.array(self.points[:-2], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(imgMain, [pts], False, (0, 0, 0), 3)
            minDist = cv2.pointPolygonTest(pts, (cx, cy), True)

            if -1 <= minDist <= 1:
                self.gameOver = True
                self.points = []
                self.lengths = []
                self.currentLength = 0
                self.allowedLength = 150
                self.previousHead = 0, 0
                self.score = 0

        return imgMain

path = "Resources/Donut.png"
game = SnakeGame(path)

while True:
    _, img = cap.read()
    img = cv2.resize(img, (1380, 720))
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)
    if hands:
        hand1 = hands[0]
        lmList = hand1["lmList"]
        pointIndex = lmList[8][:2]
        img = game.update(img, pointIndex)

    cv2.imshow("Ram", img)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):  # to get exit from the videos
        break
    if key == ord("r"):
        game.gameOver = False