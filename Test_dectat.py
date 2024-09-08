import cv2

vid = cv2.VideoCapture(0)
bg = cv2.createBackgroundSubtractorMOG2()

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    
)

def detect_bounding_box(vid):
    faces = face_classifier.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 1.1, 5, minSize=(40, 40))
 
    for (x, y, w, h) in faces:
#         Thresh = cv2.adaptiveThreshold( cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# , 255, cv2.ADAPTIVE_THRESH_MEAN_C,
#                                            cv2.THRESH_BINARY_INV, 11, 6)
        bg.apply(frame)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
        if(x != 0):
            circleX = x/2
        if(y != 0):
         circleY = y/2

        cv2.circle(frame,(x+100,y+90),5,(0, 255, 0),-1)

            #top left dectation
        if( circleX >0 and circleY< 270 and circleX <270 ):
            print("it works")
             #bottom left dectation
    return faces

while(True):
    ret, frame = vid.read(0)
    
    frame = cv2.resize(frame, (540, 540), fx = 22, fy = 11,
                         interpolation = cv2.INTER_CUBIC)
    cv2.circle(frame,(270,270),5,(0, 255, 0),-1)
    #left line
    cv2.line(frame,(0,270),(270,270),(0, 255, 0),1)
    #right Line
    cv2.line(frame,(270,270),(540,270),(0, 255, 0),1)
    #top line
    cv2.line(frame,(270,0),(270,270),(0, 255, 0),1)
    #Bottom Line
    cv2.line(frame,(270,0),(270,540),(0, 255, 0),1)

    

#     Thresh = cv2.adaptiveThreshold(    cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# , 255, cv2.ADAPTIVE_THRESH_MEAN_C,
#                                            cv2.THRESH_BINARY_INV, 3, 2)
    faces = detect_bounding_box(frame) 
    #faces xywh
    # if( faces.index(0) >0 and faces.index(2)< 270 and faces.index(0) <270 ):
    #     print("it works")
    cv2.imshow("thresh",frame)

    # print(faces[0])


    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

vid.release
cv2.destroyAllWindows