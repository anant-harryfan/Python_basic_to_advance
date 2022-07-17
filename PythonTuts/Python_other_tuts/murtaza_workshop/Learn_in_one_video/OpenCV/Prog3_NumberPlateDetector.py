import cv2
img = cv2.imread("Resources/numberplate1.png")
nosPlateCascade = cv2.CascadeClassifier(r"C:\Users\xyz\PycharmProjects\PythonTuts\Python_other_tuts\murtaza_workshop\Learn_in_one_video\OpenCV\Resources\haarcascades\haarcascade_russian_plate_number.xml")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

numberPlates = nosPlateCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in numberPlates:
    area = w*h
    print(area)
    if area > 1000:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(img, "Number Plate", (x, y-5), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)
        imgRoi = img[y:y+h, x:x+w]
        cv2.imshow("roi", imgRoi)
cv2.imshow("img", img)



cv2.waitKey(0)