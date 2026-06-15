import cv2
        
cap = cv2.VideoCapture(0)       

'''
frame = cv2.flip(src, flipCode)
    
    flipcode = -1   >>> Both direction flipped
    flipcode = 0    >>> Vertical Flip
    flipcode = 1    >>> Horizontal Flip
'''
while True:
    
    ret, frame = cap.read()     
    
    if not ret:
        print("Could not read frame")
        break
    
    frame = cv2.flip(frame, 1)
    cv2.imshow("Webcame Feed", frame)

             
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("quitting...")
        break
    
cap.release()       
cv2.destroyAllWindows()