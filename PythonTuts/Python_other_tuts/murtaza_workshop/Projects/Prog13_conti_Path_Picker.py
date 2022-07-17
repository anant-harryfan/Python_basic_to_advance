import cv2, numpy, pickle

polygons = []  # all the polygons and there points
path = []  # current single polygon

img = cv2.imread("Resources/Prog13_Videos/imgBoard.png")

# helps to find where we clicked
def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        path.append([x, y])

while True:
    # help to make circes on image whee we clicked
    for point in path:
        cv2.circle(img, point, 7, (0, 0, 0), cv2.FILLED)
        # cv2 take np.array so we convert path t np.array
    pts = numpy.array(path, numpy.int32).reshape((-1, 1, 2))
    # make polyGon
    img = cv2.polylines(img, [pts], True, (0, 0, 0), 2)
    cv2.imshow("achutam", img)
    # agar ham img pe kahi par click karte hai to ye func ca karo
    cv2.setMouseCallback("achutam", mousePoints)
    key = cv2.waitKey(1)
    # help to save poly gon in polygons list when we press s
    if key == ord("s"):
        score = int(input("Enter Score: "))
        polygons.append([path, score])
        print("Total polyGon", len(polygons))
        path = []
    if key == ord("q"):
        with open("Prog13_Poly_points", 'wb') as f:
            print(polygons)
            pickle.dump(polygons, f)
        break
