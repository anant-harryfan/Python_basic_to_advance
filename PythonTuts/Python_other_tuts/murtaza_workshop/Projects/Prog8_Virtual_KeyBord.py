import cv2
from cvzone import cornerRect
from pynput.keyboard import Key, Controller
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy


detector = HandDetector(detectionCon=0.8, maxHands=2)
# capture a video
frameWidth = 1280    # values to set width of the screen
frameHeight = 720    # values to set height of the screen
cap = cv2.VideoCapture(0)  # to capture videos
finalText = ""
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "<"],
 ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", " "],
 ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]
kb = Controller()

def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[1]))
        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return img
class Button:
    def __init__(self, pos, text, size=[85, 85]):
         self.pos = pos
         self.size = size
         self.text = text


buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 58, 100 * i + 50], key))

while True:
    success, img = cap.read()  # to read video
    img = cv2.resize(img, (frameWidth, frameHeight))  # to set height and width of the screen
    img = cv2.flip(img, 1)
    # img = detector.findHands(img)
    hands, img = detector.findHands(img, flipType=False)  # to get hands and flipType is used to get accurate left nad right hand and it wil return img
    img = drawAll(img, buttonList)

    if hands:
        hand1 = hands[0]  # 1 hand
        LnList1 = hand1["lmList"]  # List of 21 Landnarks points
        bbox1 = hand1["bbox"]  # Bounding Box info x,y,n
        for button in buttonList:  # help to draw keys on screen
            x, y = button.pos
            w, h = button.size
            # print(LnList1)
            if x < LnList1[8][0] < x+w and y < LnList1[8][1] < y+h:  # if my hand is between the button  and y change color
                cv2.rectangle(img, (x-7, y-7), (x + w+7, y + h+7), (255, 255, 255), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)
                l, info, img = detector.findDistance(LnList1[8], LnList1[12], img)
                # print(l)
                if l < 95:  # if my index finger tip and middle finger tip is lesser than 90 (any cvzone value) click the button
                    if button.text != "<":
                        kb.press(button.text)
                        cv2.rectangle(img, button.pos, (x + w, y + h), (125, 125, 125 ), cv2.FILLED)
                        cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                        finalText += button.text
                        sleep(0.30)
                        if len(finalText) == 20:
                            finalText = ""
                    elif button.text == "<":
                        kb.press(Key.backspace)
                        sleep(0.30)
                        if len(finalText) != 0:
                            le = len(finalText) - 1
                            finalText = finalText.replace(finalText[le], "")

    cv2.rectangle(img, (50, 350), (1000, 450), (0, 0, 0), cv2.FILLED)  # show what i have typed
    cv2.putText(img, finalText, (60, 425),
                cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
    cv2.imshow("video", img)    # to show video
    if cv2.waitKey(1) & 0xFF == ord('q'):   # to get exit from the videos
        break
cv2.waitKey(1)