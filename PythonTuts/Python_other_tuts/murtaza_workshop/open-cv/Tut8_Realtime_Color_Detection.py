import cv2
import numpy as np

frameHeight = 480
frameWidth = 640
cap = cv2.VideoCapture(1)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    _, img = cap.read()
    cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.imshow("Original", img)
    # cv2.imshow("OriginalHsv", imgHsv)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()