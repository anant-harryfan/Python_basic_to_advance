import cv2
import csv
from cvzone.HandTrackingModule import HandDetector
from cvzone.Utils import putTextRect
from time import sleep
# creating mcq class
class MCQ:
    def __init__(self, data):  # this is one single q
        self.Question = data[0]
        self.Choice1 = data[1]
        self.Choice2 = data[2]
        self.Choice3 = data[3]
        self.Choice4 = data[4]
        self.Answer = int(data[5])
        # initialize user ans
        self.UserAnswer = None

    def update(self, cursor, bboxs):
        # i is q nos if wee see, bbox is x,y,x1,y1 of boxes
        for i, bbox in enumerate(bboxs):
            x1, y1, x2, y2 = bbox
            # if fingers in between of box
            if x1 < cursor[0] < x2 and y1 < cursor[1] < y2:
                self.UserAnswer = i+1
                if self.UserAnswer == self.Answer:
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)
                else:
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), cv2.FILLED)




cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8)
# Importing csv file
path = "Prog12_MCQ.csv"
with open(path, newline="\n") as f:
    reader = csv.reader(f)
    # All q, choice, ans
    AllData = list(reader)[1:]  # this is all que

qNo = 0
TotalQ = len(AllData)

# creating object for each MCQ
mcqList = []
for q in AllData:
    mcqList.append(MCQ(q))


while True:
    success, img = cap.read()
    img = cv2.resize(img, (1080, 720))
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)
    if qNo < TotalQ:
        mcq = mcqList[qNo]
        # cvzone has a func putTextRect which help to put text and rectangle at one place and rectangle will auto adjust his width if the text lenght is greater of smaller
        #                     img,  text,        position is main req
        #                                                    scale, thicknessText, thicknessrec
        img, bbox = putTextRect(img, mcq.Question, [100, 100],     2, 2, offset=50, border=5)
        img, bbox1 = putTextRect(img, mcq.Choice1, [100, 250], 2, 2, offset=50, border=5)
        img, bbox2 = putTextRect(img, mcq.Choice2, [400, 250], 2, 2, offset=50, border=5)
        img, bbox3 = putTextRect(img, mcq.Choice3, [100, 400], 2, 2, offset=50, border=5)
        img, bbox4 = putTextRect(img, mcq.Choice4, [400, 400], 2, 2, offset=50, border=5)

        if hands:
            lmList = hands[0]["lmList"]
            cursor = lmList[8]
            l, info = detector.findDistance(lmList[8], lmList[12])
            if l < 50:
                # see that user click right an or not
                mcq.update(cursor, [bbox1, bbox2, bbox3, bbox4])
                if mcq.UserAnswer is not None:
                    sleep(0.3)
                    qNo += 1
    else:
        score = 0
        for mcq in mcqList:
            if mcq.Answer == mcq.UserAnswer:
                score += 1

            img, _ = putTextRect(img, "Quiz Completed", [150, 300], 2, 2, offset=50, border=5)
            img, _ = putTextRect(img, f"Your Score: {score}/{TotalQ}", [600, 300], 2, 2, offset=50, border=5)
    # Progress Bar
    BarValue = 150 + (750//TotalQ)*qNo
    if qNo == TotalQ:
        cv2.rectangle(img, (150, 600), (900, 650), (0, 255, 0), cv2.FILLED)
    cv2.rectangle(img, (150, 600), (BarValue, 650), (0, 255, 0), cv2.FILLED)
    cv2.rectangle(img, (150, 600), (900, 650), (0, 0, 0), 5)
    img, _ = putTextRect(img, f"{round((qNo/TotalQ)*100)}%", [950, 635], 2, 2, offset=16)
    cv2.imshow("Ram", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # to get exit from the videos
        break