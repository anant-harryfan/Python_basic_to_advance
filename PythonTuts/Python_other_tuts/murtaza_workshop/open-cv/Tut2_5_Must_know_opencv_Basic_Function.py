import cv2
import numpy as np

# img = cv2.imread("itachi_uchiha.jpg", 0)  # if we put 0 after this image will change to black and white
img = cv2.imread("Tut1_itachi_uchiha.jpg")  # if we put 0 after this image will change to black and white
# cv2.imshow("Itachi", img)

# COLOR CHANGER
# if you want to image in many other colour there is the code
# imgcol = cv2.cvtColor(img, cv2.COLOR_and the color you want)
# imgcol = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow("ItachiI", imgcol)

# BLUR IMAGE
# Blur_image = cv2.GaussianBlur(img, (79, 79), 0)  # blur the image but only in odd numbers can change the blurriness of image
# cv2.imshow("Itachi_blur", Blur_image)

# Outlines or edges of image
outing = cv2.Canny(img, 100, 100)
# cv2.imshow("Itachi_at_the_edge", outing)

# img dilation and erosion
# commonly done on canny images
kernal = np.ones((5, 5), np.uint8)
# print(kernal)
# imgDilation = cv2.dilate(outing, kernal, iterations=1)  # the big iteration nos is the big effect it make
imgDilation = cv2.dilate(img, kernal, iterations=1)  # the big iteration nos is the big effect it make
cv2.imshow("Itachi_at_the_edge2", imgDilation)
# imgErosin = cv2.erode(imgDilation, kernal, iterations=3)  # thin out all the edges
imgErosin = cv2.erode(img, kernal, iterations=3)  # thin out all the edges
cv2.imshow("Itachi_at_the_edge_end", imgErosin)


cv2.waitKey(0)