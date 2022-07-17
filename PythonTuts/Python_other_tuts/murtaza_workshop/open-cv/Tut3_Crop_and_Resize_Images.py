import cv2

img = cv2.imread("Tut1_itachi_uchiha.jpg")
# shows image height and width
print(img.shape)

w, h = 1000, 600
# resize image
imgResize = cv2.resize(img, (w, h))
print(imgResize.shape)

# crop image
#                  h    ,     w
imgCropped = img[300:470, 1100:1280]

# after cropped if we have to resize image with same w and h of original image we can do by this
imgCropResize = cv2.resize(imgCropped, (img.shape[1], img.shape[0]))

cv2.imshow("Itachi", img)
# cv2.imshow("Itachii", imgResize)
cv2.imshow("Itachiii", imgCropped)  # akela sharingan kiya isme mane
cv2.imshow("Itachiiii", imgCropResize)  # akela sharingan kiya isme mane
cv2.waitKey(0)