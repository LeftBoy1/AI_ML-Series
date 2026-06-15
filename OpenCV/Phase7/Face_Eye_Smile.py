import cv2

face_cascade = cv2.CascadeClassifier("F:\\Devansh_Gupta\\AI + ML\\OpenCV\\Phase7\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("F:\\Devansh_Gupta\\AI + ML\\OpenCV\\Phase7\\haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("F:\\Devansh_Gupta\\AI + ML\\OpenCV\\Phase7\\haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)  
    
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y) ,(x + w , y + h) , (0,100,255), 2 )
        
        roi_gray = gray[y:y+h , x:x+w]
        roi_color = frame[y:y+h , x:x+w]           #roi (Region of Interest) -  helps to detect only useful things(which we wants to detect like-object)
        
        
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        if len(eyes)> 0:
            cv2.putText(frame, "Eyes Detected", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,100,255), 2)       #(x, y-30) is written to shift a text littlebit and preventing overlap with rectangle 
        
        
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)
        if len(smiles)> 0:
            cv2.putText(frame, "Smile Detected", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,100,255), 2)
            
            
        
           
    cv2.imshow("Smart Detection", frame)

    
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()       
cv2.destroyAllWindows()