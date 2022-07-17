import pickle
import cv2

try:
    with open("Resources/Prog17_CarParkProject/CarParkPos", "rb") as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseClick(events, x, y, flags, param):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y + height:
                posList.pop(i)
    with open("Resources/Prog17_CarParkProject/CarParkPos" , "wb") as f:
        pickle.dump(posList, f)

width, height = 107, 48
while True:
    img = cv2.imread("Resources/Prog17_CarParkProject/carParkImg.png")
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), (255, 0, 0), 4)
    cv2.imshow("Ram", img)
    cv2.setMouseCallback("Ram", mouseClick)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # to get exit from the videos
        break