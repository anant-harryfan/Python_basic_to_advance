import cvzone.Utils
import cv2
from numpy import zeros, uint8
###############################  overlay Png ######################################
# background image
# ImgBack = cv2.imread("0.Resources_GameDev/Prog7_Images/nature.jpg")
# if you want it on a plain color image
# ImgBack = zeros((480, 640, 3), np.uint8)
# overlay image
# ImgFront = cv2.imread("0.Resources_GameDev/Prog7_Images/gear.png", cv2.IMREAD_UNCHANGED)
# if you want to resize it
# ImgFront = cv2.resize(ImgFront, (0, 0), None, 0.5, 0.5)
# final result
# ImgResult = cvzone.overlayPNG(ImgBack, ImgFront, [20, 20])
# cv2.imshow("ImgBack", ImgBack)
# cv2.imshow("ImgResult", ImgResult)
# cv2.waitKey(0)
#####################################################################################

################################# Logo Overlay ######################################
# # background image
# ImgBack = cv2.imread("0.Resources_GameDev/Prog7_Images/pc.jpg")
# # overlay image
# ImgFront = cv2.imread("0.Resources_GameDev/Prog7_Images/logo.png", cv2.IMREAD_UNCHANGED)
# # if you want to resize it
# ImgFront = cv2.resize(ImgFront, (0, 0), None, 0.2, 0.2)
# # auto matic bringing logo at bottom/
# hf, wf, cf = ImgFront.shape
# hb, wb, cb = ImgBack.shape
# # final result
# ImgResult = cvzone.overlayPNG(ImgBack, ImgFront, [0, hb-hf])
# # cv2.imshow("ImgBack", ImgBack)
# cv2.imshow("ImgResult", ImgResult)
# cv2.waitKey(0)
#####################################################################################

################################## webcam overlay ###################################
# background image
# cap = cv2.VideoCapture(0)
# success, img = cap.read()
# overlay image
# ImgFront = cv2.imread("0.Resources_GameDev/Prog7_Images/logo.png", cv2.IMREAD_UNCHANGED)
# if you want to resize it
# ImgFront = cv2.resize(ImgFront, (0, 0), None, 0.3, 0.3)
# # auto matic bringing logo at bottom/
# hf, wf, cf = ImgFront.shape
# hb, wb, cb = img.shape
# while True:
    # success, img = cap.read()
    # final result
    # ImgResult = cvzone.overlayPNG(img, ImgFront, [0, hb-hf])
    # cv2.imshow("ImgResult", ImgResult)
    # cv2.waitKey(1)
#####################################################################################

################################### Image Rotation ##################################
def empty(a):
    pass
angle = 0
cv2.namedWindow("Parameter")
cv2.resizeWindow("Parameter", 640, 100)
cv2.createTrackbar("Speed", "Parameter", 1, 25, empty)
while True:
    # background image
    ImgBack = zeros((500, 880, 3), uint8)*255
    # overlay image
    val = cv2.getTrackbarPos("Speed", "Parameter")
    ImgG1 = cv2.imread("Resources/Prog7_Images/gear.png", cv2.IMREAD_UNCHANGED)
    ImgG2 = ImgG1.copy()
    ImgG1 = cvzone.rotateImage(ImgG1, angle+23)
    ImgG2 = cvzone.rotateImage(ImgG2, -angle)
    angle += val

    # final result
    ImgResult = cvzone.overlayPNG(ImgBack, ImgG1, [125, 20])
    ImgResult = cvzone.overlayPNG(ImgResult, ImgG2, [400, 20])
    # cv2.imshow("ImgBack", ImgBack)
    cv2.imshow("ImgResult", ImgResult)
    cv2.waitKey(1)
#####################################################################################