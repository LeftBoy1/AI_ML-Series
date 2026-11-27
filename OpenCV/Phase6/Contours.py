# Contours are used to detect and describe the shape/boundary of objects in an image. line drawn around the edge of a shape

# counters, hierarchy = cv2.findContours(image, mode, method)
# cv2.drawContours(image, contours, contours_index, color, thickness)

'''
1. Contours
Contours are the detected boundaries of objects in an image, represented as a collection of coordinates (points).

For example, suppose your image contains:
- One circle
- One rectangle
- One triangle
OpenCV detects their boundaries and stores them inside contours.


2. Hierarchy
Hierarchy describes the relationship between different contours.

For example, imagine a white rectangle containing a black circle, which contains a white smaller circle.

There are outer and inner boundaries.

Hierarchy helps OpenCV identify which contour:
- Is the parent of another contour.
- Is a child of another contour.
- Has a next or previous sibling.


3. Mode (Retrieval Mode)
Mode determines which contours OpenCV should retrieve and how their hierarchy should be maintained.

There are four commonly used modes:
Mode	Meaning
cv2.RETR_TREE	= Retrieves all contours with complete hierarchy.
cv2.RETR_EXTERNAL	= Retrieves only outermost contours.
cv2.RETR_LIST	= Retrieves all contours without hierarchy relationships.
cv2.RETR_CCOMP	= Retrieves contours in a two-level hierarchy.


4. Method (Contour Approximation Method)
Method determines how much detail or how many points should be stored to represent a contour.
METHOD - How many points should be stored?

Two commonly used methods:

A. cv2.CHAIN_APPROX_NONE
- Stores all boundary points.
- Requires more memory.
B. cv2.CHAIN_APPROX_SIMPLE
- Removes unnecessary intermediate points.
- Stores only important points.
- Requires less memory.



'''
import cv2

image = cv2.imread("D:\\Devansh_Gupta\\AI + ML\\OpenCV\\Phase6\\shapeS.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh =  cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

'''Finding Contours'''
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1,  (0,255,0) , 4)   #-1 means “draw ALL contours.


cv2.imshow("Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

