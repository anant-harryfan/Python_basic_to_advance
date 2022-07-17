import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector()
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
startDistance = None
scale = 0
cx, cy = 100, 100
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1080, 520))
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)
    img1 = cv2.imread("Resources/Prog10_Zoomed.jpg")

    if len(hands) == 2:
        if detector.fingersUp(hands[0]) != [0, 0, 0, 0, 0] and detector.fingersUp(hands[1]) != [0, 0, 0, 0, 0]:
            # print("Zoomed")
            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]
            if startDistance is None:
                # zoom by fingers (not recommended)
                # l, _, img = detector.findDistance(lmList1[8], lmList2[8], img)
                # zoom by hately (recommended)
                l, _, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
                startDistance = l
            # zoom by fingers (not recommended)
            # l, info, img = detector.findDistance(lmList1[8], lmList2[8], img)
            # zoom by hately (recommended)
            l, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
            scale = int((l - startDistance) // 2)
            cx, cy = info[4:]

            print(scale)
    else:
        startDistance = None
    try:
        h1, w1, _ = img1.shape
        newH, newW = ((h1+scale)//2)*2, ((w1+scale)//2)*2
        img1 = cv2.resize(img1, (newH, newW))
        img[cy-newH//2: cy+newH//2, cx-newW//2: cx+newW//2] = img1
    except:
        pass
    cv2.imshow("img", img)
    cv2.waitKey(1)