import cv2
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1380, 720))
    img = cv2.flip(img, 1)
    cv2.imshow("Ram", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # to get exit from the videos
        break

# Hand tracking
# import cv2
# from cvzone.HandTrackingModule import HandDetector
#
# cap = cv2.VideoCapture(0)
# detector = HandDetector()
#
# while True:
#     _, img = cap.read()
#     img = cv2.resize(img, (1380, 720))
#     img = cv2.flip(img, 1)
#     hands, img = detector.findHands(img, flipType=False)
#     if hands:
#         hand1 = hands[0]
#         lmList = hand1["lmList"]
#         bbox = hand1["bbox"]
#         cx, cy = hand1["center"]
#
#     cv2.imshow("Ram", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):  # to get exit from the videos
#         break