import cv2
# import numpy as np
# from cvzone import stackImages
# cap = cv2.VideoCapture(0)  # capture webcam , video if we give path
# img = cv2.imread("0.Resources_GameDev/itachi_uchiha.jpg")  # read the image

# kernal = np.ones((5, 5), np.uint8)
# cap.set(3, 456)  # 3 is id of width
# cap.set(4, 456)  # 4 is id of height
# cap.set(10, 100)  # 10 is id of brightness

# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # change the color of the image
# imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)  # make the img gray
                          # to make less outlines you can increase it or to make more boundaries you can decrease it
# imgCanny = cv2.Canny(img, 100, 100)  # Draws the boundaries means outline of the image
# imgCannyDilation = cv2.dilate(imgCanny, kernal, iterations=1)  # it make the boundaries thicker by which comp can recognize the line
# imgCannyErode = cv2.erode(imgCannyDilation, kernal, iterations=1)  # do the oppo of dilation it make the boundaries thinner

# cv2.imshow("GrayImage", imgGray)
# cv2.imshow("BlurImage", imgBlur)
# cv2.imshow("CannyImage", imgCanny)
# cv2.imshow("DilateCannyImage", imgCannyDilation)
# cv2.imshow("ErodeCannyImage", imgCannyErode)
# imgList = [img, imgGray, imgBlur, imgCanny, imgCannyDilation, imgCannyErode]
#
# crop and resize images
# print(img.shape)  # tell the size of image
# it will return for this image  is (720, 1280, 3) where 720 is height, 1280 is width and 3 is channel which is bgr (blue, green, red)

# imgResize = cv2.resize(img, (400, 200))  # help to resize image where 400 is width, 200 is height
# cv2.imshow("imgResize", imgResize)

# as image is a bundle of list or array we can cropped it my list slicing method
# imgCropped = img[0:200, 200:400]  # where 0:200 is height and 200:400 is width
# cv2.imshow("imgCropped", imgCropped)

# shape and text
# creates a blank black img
# img = np.zeros((512, 512, 3), np.uint8)

# img[:] = 255, 0, 0  # make the whole image as blue   # just like list slicing
# img[100:200, 200:300] = 255, 0, 0  # make a specific part of image as blue   # just like list slicing
            # img  from were we have to start to   the point we have to end line  color         thickness                # same with rectangle
# cv2.line(img, (0, 0),                         (300, 300),                       (255, 0, 255), 3)  # creates an line on the image
# cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (255, 0, 255), 3)  # creates a line on the image from minimum value (0, 0) to maximum value (512, 512)
# cv2.rectangle(img, (0, 0), (300, 400), (255, 255, 0), 3)  # creates a rectangle   # to fill whole area use cv2.FILLED in place of thickness
          # img, center point   radius  color         thickness
# cv2.circle(img, (100, 300),    50,      (0, 255, 255), 3) # creates a circle # to fill whole area use cv2.FILLED in pace of thickness
# cv2.putText(img, "Anant the coder", (20, 230), cv2.FONT_ITALIC, 1, (0, 0, 255), 2)

# Bird view
# img = cv2.imread("0.Resources_GameDev/cards.jpg")
# width, height = 250, 350
#
# pts1 = np.float32([[63, 120], [156, 104], [84, 264], [191, 241]])  # all points
# pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])  # 2nd img that will give perspective view
# print(pts1[0][0])
# matrix = cv2.getPerspectiveTransform(pts1, pts2)   # to get it straight
# imgstack = cv2.warpPerspective(img, matrix, (width, height))  # give us bird view
# cv2.imshow("stacked", imgstack)

# stack images
# img = cv2.imread("0.Resources_GameDev/itachi_uchiha.jpg")
# img2 = cv2.imread("0.Resources_GameDev/cards.jpg")
# imgList=[img2, img2]
# allImg = stackImages(scale= 1, _imgList=imgList, cols=2)  # come in cvzone module
# cv2.imshow("all", allImg)
# print(img.shape, img2.shape)

# color detection
# def empty(a):  # to create a empty function
#     pass
# cv2.namedWindow("TrackBars")  # create a new windows named as trackBars
# cv2.resizeWindow("TrackBars", 640, 400)  # resize window
#                 name of value , old window named (trackbars), initial value, maximum value, a function
# cv2.createTrackbar("Hue Min", "TrackBars",                       0,           179, empty)  # create a trackbars    # in opencv only 179 value are there in maximum value
# cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
# cv2.createTrackbar("Sat Min", "TrackBars", 81, 255, empty)
# cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
# cv2.createTrackbar("Val Min", "TrackBars", 166, 255, empty)
# cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

# shape detection
# def getContours(img):
#     contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         print(area)
#         if area > 500:
#             cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
#             peri = cv2.arcLength(cnt, True)
#             print(peri)
#             approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
#             print(len(approx))
#             objCor = len(approx)
#             x, y, w, h = cv2.boundingRect(approx)
#
#             if objCor == 3:
#                 objectType = "Tri"
#             elif objCor == 4:
#                 aspRatio = w / float(h)
#                 if aspRatio > 0.98 and aspRatio < 1.03:
#                     objectType = "Square"
#                 else:
#                     objectType = "Rectangle"
#             elif objCor > 4:
#                 objectType = "Circles"
#             else:
#                 objectType = "None"
#
#             cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
#             cv2.putText(imgContour, objectType,
#                         (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.46,
#                         (0, 0, 0), 2)
#
#
# img = cv2.imread("0.Resources_GameDev/shapes.jpg")
# imgContour = img.copy()
#
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
# imgCanny = cv2.Canny(imgBlur, 50, 50)
# getContours(imgCanny)
#
# imgStack = stackImages([img, imgGray, imgBlur, imgCanny, imgContour], scale=1, cols=3)
# cv2.imshow("stacked", imgStack)
# getContours(imgCanny)

# face detection on a image or video
# faceCascade= cv2.CascadeClassifier("0.Resources_GameDev/haarcascades/haarcascade_frontalface_default.xml")
# img = cv2.imread('0.Resources_GameDev/lena.png')
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# faces = faceCascade.detectMultiScale(imgGray,1.1,4)
#
# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#
# while True:
#     success, img = cap.read()  # to read video success is a bool value that we are success to get img , video and img is the original image
    ####################### color detector ################################
    # img = cv2.imread("0.Resources_GameDev/lambo.jpg")
    # imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # change img to hsv
    # h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")  # help to get trackbars position numbers
    # h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    # s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    # s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    # v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    # v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    # print(h_min, h_max, s_min, s_max, v_min, v_max)
    # lower = np.array([h_min, s_min, v_min])  # all min values
    # upper = np.array([h_max, s_max, v_max])  # all values of max hue saturation and v
    # mask = cv2.inRange(imgHSV, lower, upper)  # create the mask from img
    # imgResult = cv2.bitwise_and(img, img, mask=mask)  # create a new image
    # allImg = stackImages([img, imgHSV, mask, imgResult], 2, 1)
    # cv2.imshow("imgHSV", imgHSV)
    # cv2.imshow("MASK", mask)
    # cv2.imshow("imgResult", imgResult)
    # cv2.imshow("allImg", allImg)
    #########################################################################

    # cv2.imshow("Video or img", img)  # show thee image

    # this if statement help to exit program when we press q
    # if cv2.waitKey(1) & 0xFF == ord("q"):  # stop image for milliSec if 0 it will be infinite and 1000 = 1sec
    #     break
