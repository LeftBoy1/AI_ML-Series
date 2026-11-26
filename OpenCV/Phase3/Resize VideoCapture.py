import cv2

cap = cv2.VideoCapture(0)

# Set width and height BEFORE the loop
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    cv2.imshow("Resized Capture", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



        # OR    

import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not read frame")
        break

    # Resize captured frame
    resized_frame = cv2.resize(frame, (640, 480))

    cv2.imshow("Resized Webcam", resized_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()