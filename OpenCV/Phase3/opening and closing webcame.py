import cv2

# cap = cv2.VideoCapture(source)
        #source = 0 >>> if using laptops or built-in cameras
        #source = 1 >>> i fusing external webcame
        
cap = cv2.VideoCapture(0)       #starts the capturing


while True:
    
    #success, image = cap.read()     
    ret, frame = cap.read()         #ret = return "True/False" status that image is reading or not  ,   frame = image
    
    if not ret:
        print("Could not read frame")
        break
    
    cv2.imshow("Webcame Feed", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("quitting...")
        break
    
cap.release()       #stopping capturing
cv2.destroyAllWindows()
