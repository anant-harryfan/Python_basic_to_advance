import cv2
import numpy as np

# create a blank image
img = np.zeros((512, 512, 3), np.uint8)  # np.unit8 will change our value to int from float
# for color we have from 0 to 255 where 255 is blue
# print(img)
# print(img.shape)
# img[:] = 255, 0, 0  # change the color of whole photo
# as we know in by [] we can crop image so we can also change color of that region by this
# img[200:500, 200:500] = 255, 0, 0  # change the color of specific part of photo

# create a line on a image
#        img,   origin,   from where to start and end,    color,    thickness
cv2.line(img,   (0, 0),    (img.shape[1], img.shape[0]),   (0, 255, 0),   7)

# create a square and rectangle
# cv2.rectangle(img, (350, 100), (500, 200), (0, 0, 255), 2)
# if you want to fill the box just insted of thinckness just type cv2.FILLED
cv2.rectangle(img, (350, 100), (500, 200), (0, 0, 255), cv2.FILLED)

# create a circle
#          img, center point, radius, color,   thickness or cv2.FILLED
cv2.circle(img, (150, 400),    80,   (255, 0, 0),    2)

# put text
#           img,  text,          where we want text, font,         scale, color,     thickness
cv2.putText(img, "CodeWithHarry", (75, 50),         cv2.FONT_ITALIC, 1,  (0, 250, 350),      1)

cv2.imshow("img", img)

cv2.waitKey(0)
