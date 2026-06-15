import cv2
# Contours are used to detect and describe the shape/boundary of objects in an image. line drawn around the edge of a shape
# counters, hierarchy = cv2.findContours(image, mode, method)
        # counters = list of all detected outlines
        # hierarchy = relationship between counters
        # image= provided image should be in binary(black or white)
        # mode(retreival mode) = how many and what kind of counters have to return
            # a.) Retreival_Tree = return all shapes with heirarchy
            # b.) Retreival_External = return outermost shapes
            # c.) Retreival_List = return all shapes without heirarchy
            
        #method = how much detail is return of a counter
        

# cv2.drawContours(image, contours, contours_index, color, thickness)



image = cv2.imread("F:\\Devansh_Gupta\\AI + ML\\OpenCV\\Phase4\\o.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh =  cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

'''Finding Contours'''
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1,  (0,255,0) , 4)   #-1 means “draw ALL contours.


cv2.imshow("Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

