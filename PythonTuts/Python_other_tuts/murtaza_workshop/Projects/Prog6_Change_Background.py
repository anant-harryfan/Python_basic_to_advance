from cvzone.SelfiSegmentationModule import SelfiSegmentation as sus
import cv2
import cvzone
from os import listdir


segmentor = sus()
cap = cv2.VideoCapture(0)
fps = cvzone.FPS()
ImgName = listdir(r"C:\Users\xyz\PycharmProjects\PythonTuts\Python_other_tuts\murtaza_workshop\Projects\Resources\Prog6_background\img")
ImgList = []
for imgPath in ImgName:
    imgs = cv2.imread(f"Resources/Prog6_background/img/{imgPath}")
    ImgList.append(imgs)
# print(len(ImgList))
IndexImg = 0
while True:
    success, img = cap.read()
    # success2, lol = video.read()
    lol = cv2.resize(ImgList[IndexImg], (1380, 720))
    img = cv2.resize(img, (1380, 720))
    img = cv2.flip(img, 1)
    # print(IndexImg)imgOut = segmentor.removeBG(img, lol, threshold=0.5)
    imgOut = segmentor.removeBG(img, lol, threshold=0.5)

    stacked = cvzone.stackImages([img, imgOut], 2, 0.5)
    _, stacked = fps.update(stacked)
    # cv2.imshow("img", img)
    # cv2.imshow("imgOut", imgOut)
    cv2.imshow("Stacked", stacked)
    key = cv2.waitKey(1)
    if key == ord('a'):
        if IndexImg>0:
            IndexImg -= 1
    if key == ord('d'):
        if IndexImg < len(ImgList)-1:
            IndexImg += 1
    if key == ord('q'):
        break


