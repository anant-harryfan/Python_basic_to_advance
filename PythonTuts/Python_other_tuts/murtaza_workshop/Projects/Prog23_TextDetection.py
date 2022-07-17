import cv2
import pytesseract
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1380, 720))
    img = cv2.flip(img, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print(pytesseract.image_to_string(img))
    cv2.imshow("Ram", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # to get exit from the videos
        break