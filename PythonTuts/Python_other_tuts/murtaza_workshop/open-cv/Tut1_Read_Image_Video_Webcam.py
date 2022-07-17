import cv2

# read a image
# img = cv2.imread("itachi_uchiha.jpg")  # To read image
# cv2.imshow("Itachi", img)  # To show image
# cv2.waitKey(0) # To wait the image otherwise it will be close (0 means infinity)

# capture a video
frameWidth = 1280    # values to set width of the screen
frameHeight = 720    # values to set height of the screen
videoos = cv2.VideoCapture(0)  # to capture videos
# videoos.set(3, frameWidth)  # to set width of the screen
# videoos.set(4, frameHeight)  # to set height of the screen
while True:
    sucess, img = videoos.read()  # to read video
    img = cv2.resize(img, (frameWidth, frameHeight))  # to set height and width of the screen
    cv2.imshow("video", img)    # to show video
    if cv2.waitKey(1) & 0xFF == ord('q'):   # to get exit from the videos
        break
cv2.waitKey(1)