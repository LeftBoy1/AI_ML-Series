import cv2

img = cv2.imread("F:\\Devansh_Gupta\\AI + ML\\OpenCV\\Phase 1\\o.jpg")

# cv2.circle(img, centre, radius, color, thickness)
    
    #thickness = -1  >>>inner filled circle
    
    

#CIRCLE 1
centre = (600,350)
color = (0,0 ,255)      
radius = 70
cv2.circle(img, centre, radius, color, 3)
cv2.imshow("Circle",img)


#CIRCLE 2
centre = (700,450)
color = (255,0 ,0)      
radius = 70
cv2.circle(img, centre, radius, color, -1)
cv2.imshow("Circle",img)


#CIRCLE 3
centre = (800,550)
color = (0,255 ,0)      
radius = 70
cv2.circle(img, centre, radius, color, 3)
cv2.imshow("Circle",img)



cv2.waitKey(0)
cv2.destroyAllWindows()