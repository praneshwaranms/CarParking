import cv2


cap = cv2.VideoCapture(1)

while True:
    success , img = cap.read()
    cv2.imshow("Image", img)
    # cv2.imshow("ImageBlur", imgBlur)
    # cv2.imshow("ImageThres", imgMedian)
    cv2.waitKey(10)