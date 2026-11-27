''' edges = cv2.Canny(image, threshold1, threshold2)
        #threshold1 = lower boundary
        #threshold2 = upper boundary

A threshold is a limit or boundary value used to decide whether a pixel should be considered part of an edge or not.
This threshold is different from image thresholding, here we are detecting edges in an image

Ranges:-
50, 100	        Detects more edges, including weaker ones
100, 200	Balanced edge detection
150, 250	Detects fewer, stronger edges
'''
import cv2

image = cv2.imread("D:\\Devansh_Gupta\\AI + ML\\OpenCV\\Phase4\\o.jpg", cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(image, 50,150)       

cv2.imshow("original", image)
cv2.imshow("Canny Edge", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
