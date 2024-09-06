import cv2

vid = cv2.VideoCapture(0)
bg = cv2.createBackgroundSubtractorMOG2()
bg2 = cv2.createBackgroundSubtractorKNN()

while(True):
    ret, frame = vid.read(0)
    frame = cv2.resize(frame, (540, 380), fx = 22, fy = 11,
                         interpolation = cv2.INTER_CUBIC)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                           cv2.THRESH_BINARY_INV, 11, 2)
    cv2.imshow('Thresh', Thresh)
    Thresh2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                           cv2.THRESH_BINARY, 11, 2)
    cv2.imshow('Threshw', Thresh2)
    # cv2.imshow("test2",bg2.apply(frame))
    #cv2.imshow("bg1",bg.apply(frame))
    cv2.imshow("bg2",bg2.apply(frame))
    cv2.imshow("Og",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

vid.release
cv2.destroyAllWindows