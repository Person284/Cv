import cv2

vid = cv2.VideoCapture(1)
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    
)

def detect_bounding_box(vid):
    faces = face_classifier.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 1.1, 5, minSize=(40, 40))
 
    for (x, y, w, h) in faces:
        Thresh = cv2.adaptiveThreshold( cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                           cv2.THRESH_BINARY_INV, 11, 6)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)

        # cv2.circle(vid,(x/2,y/2),1,(255, 0, 0),1)
    return faces

while(True):
    ret, frame = vid.read(1)
    
#     Thresh = cv2.adaptiveThreshold(    cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# , 255, cv2.ADAPTIVE_THRESH_MEAN_C,
#                                            cv2.THRESH_BINARY_INV, 3, 2)

    faces = detect_bounding_box(frame) 
   
    cv2.imshow("thresh",frame)
    print(faces)


    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

vid.release
cv2.destroyAllWindows