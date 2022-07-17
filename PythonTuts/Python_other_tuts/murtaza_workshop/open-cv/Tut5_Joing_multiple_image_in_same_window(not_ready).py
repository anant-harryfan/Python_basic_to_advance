import cv2
import numpy as np

# def stackImages(scale, imgArray):
#                len(imgarray)
#                len(imgarray[0])
#      rows -
#      cols -
#      rowsAvailable = isinstance(imgArray[0], list)
#      width = imgarray[@][0].shape[1]
#      height = ingarray[0][0]. shape[o]
#      if rowsAvailable:
#            for x in range_(0, rows):
#                 for y in range(e, cols):
#                       if imgarray[x][y]. shape[:2] == imgArray[@][@].shape_[:2]:
#                            imgArray[x][y] = cv2.resize(imgArray[x][y], (e, 0), None, scale, scale)
#                       else:
#                            imgArray[x][y] - cv2.resize(imgArray[x][yl, (imgArray[@][0]. shape[1], ingArray[0][0]. shape[@]), None, scale, scale
#                       if len(imgarray[x]ly).shape) -- 2: imgArray[x][y]; cv2.cvtcolor(_imgArray[x][y], cv2.COLOR_GRAY2BGR)
#            imageBlank - np.zeros ( (height, width, 3), np.uint8)
#            hor = [imageBlank]*rows
#            hor con = [imageblank]"rows
#            for x in range (e, rows):
#                hor [x] - np.hstack(ingarray[x])
#            ver - np.vstack(hor)




img = cv2.imread("Tut1_itachi_uchiha.jpg")  # if we put 0 after this image will change to black and white
# cv2.imshow("Itachi", img)

imgcol = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow("ItachiI", imgcol)

Blur_image = cv2.GaussianBlur(img, (79, 79), 0)
# cv2.imshow("Itachi_blur", Blur_image)

outing = cv2.Canny(img, 100, 100)
# cv2.imshow("Itachi_at_the_edge", outing)

kernal = np.ones((5, 5), np.uint8)
# print(kernal)
imgDilation = cv2.dilate(img, kernal, iterations=1)
# cv2.imshow("Itachi_at_the_edge2", imgDilation)
imgErosin = cv2.erode(img, kernal, iterations=3)
# cv2.imshow("Itachi_at_the_edge_end", imgErosin)

# StackImages = stackImages(0.8, ([img, imgcol]))
# cv2.imshow("itachi stacked", StackImages)

cv2.waitKey(0)