import cv2

# approxPolyDP() is used to simplify a contour into a polygon with fewer points while keeping the shape almost the same
# approx = cv2.approxPolyDP(contour, epsilon, True)

image = cv2.imread("F:\\Devansh_Gupta\\AI + ML\\OpenCV\\Phase6\\shapes.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh =  cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

'''Finding Contours'''
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1,  (0,255,0) , 4)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    
    corners = len(approx)
    
    if corners ==3:
        shape_name = "Triangle"
    
    elif corners > 5:
        shape_name = "Circle"
        
    elif corners ==4:
        shape_name = "Rectangle"
        
    elif corners ==5:
        shape_name = "Pentagon"
        
    else:
        shape_name = "Unknown"
        
    cv2.drawContours(image, [approx], 0,  (0,255,0) , 4)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    cv2.putText(image, shape_name, (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0), 2)
    
cv2.imshow("Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
