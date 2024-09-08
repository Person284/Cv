import cv2
vid = cv2.VideoCapture(0)

while(True):
    ret, frame = vid.read(0)
    cv2.imshow("frame",frame)

    frame = cv2.resize(frame, (540, 380), fx = 22, fy = 11,
                         interpolation = cv2.INTER_CUBIC)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                           cv2.THRESH_BINARY_INV, 11, 2)
    cv2.imshow('Thresh', Thresh)
    gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Thresh2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                           cv2.THRESH_BINARY,11,2)
    cv2.imshow('Thresh2', Thresh2)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

vid.release
cv2.destroyAllWindows