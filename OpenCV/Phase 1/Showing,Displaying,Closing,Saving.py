import cv2

img = cv2.imread(r"F:\Devansh_Gupta\AI + ML\OpenCV\Phase 1\o.jpg")
#  imread() is used to load an image.   

cv2.imshow("Opencv", img) #display the window(image),  window is title of window
cv2.waitKey(0)    #waits until any key is pressed
cv2.destroyAllWindows()         #closes the window(image)
cv2.imwrite("output.jpg", img)  #saving file

if img is None:
    print("Error:")
else:
    print("Generated!!")