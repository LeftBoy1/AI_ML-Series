import cv2
cap = cv2.VideoCapture(0)

# cv2.VideoWriter(filename, codec, fps, frame_size)       #to save webcam video to a file
        #codec = compression format
        #frame_size = width , height
        
        
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))            #width of a frame
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))          #height of a frame

codec = cv2.VideoWriter_fourcc(*'XVID')     #compression format
recorded = cv2.VideoWriter("myVideo.mp4", codec, 20,(frame_width , frame_height))

while True:
    success , image = cap.read()
    
    if not success:
        break
    
    recorded.write(image)
    
    cv2.imshow("Recording_Live", image)
    
    if cv2.waitKey(1) & 0xff ==ord ('q'):
        break

cap.release()
recorded.release()
cv2.destroyAllWindows()