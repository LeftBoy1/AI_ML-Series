import cv2

face_cascade = cv2.CascadeClassifier("F:\\Devansh_Gupta\\AI + ML\\OpenCV\\Phase7\\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)                              
    '''detectMultiScale() - scan and detects face
        
        scale factor - 1.1
        
        minNeighbours- 5'''
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y) ,(x+w , y+h) , (0,100,255), 2 )

        
        
        '''(x,y) = top-left corner of rectangle
           (x+w , y+h) = bottom-right corner of rectangle
           x = how far from left
           y = how far from top
           w = width of face
           h = height of face'''
           
    cv2.imshow("The Camera1", frame)

    
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()       
cv2.destroyAllWindows()