import cv2
cap = cv2.VideoCapture(0)

# cv2.VideoWriter(filename, codec, fps, frame_size)       #cv2.VideoWriter() creates and initializes the video file.
        #codec = compression format
        #frame_size = width , height
        
        
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))            #width of a frame
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))          #height of a frame

codec = cv2.VideoWriter_fourcc(*'XVID')     #compression format

'''
    Formats to save video file:
        H.264 (avc1)
        H.265 (hvc1)
        MP4V (mp4v)
        XVID (XVID)
'''
recorded = cv2.VideoWriter("myVideo.mp4", codec, 400,(frame_width , frame_height))

while True:
    success , image = cap.read()
    
    if not success:
        break
    
    recorded.write(image)   # it actually saves each captured webcam frame into the video file.
    
    cv2.imshow("Recording_Live", image)
    
    if cv2.waitKey(1) & 0xff ==ord ('q'):
        break

cap.release()
recorded.release()
cv2.destroyAllWindows()

#cv2.VideoWriter() creates and initializes the video file, whereas recorded.write(image) adds individual frames to that video file.