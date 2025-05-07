import cv2
import pickle

width, height = 90, 185
# cap = cv2.VideoCapture(1)
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)


while True:
    # success, image = cap.read()
    image = cv2.imread(r"IMG20240128211551.jpg")
    img = cv2.resize(image, (800, int(image.shape[0] * (800 / image.shape[1]))))
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (0, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break