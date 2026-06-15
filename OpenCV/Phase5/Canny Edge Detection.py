import cv2

# edges = cv2.Canny(image, threshold1, threshold2)
        #threshold1 = lower boundary
        #threshold2 = upper boundary

image = cv2.imread("F:\\Devansh_Gupta\\AI + ML\\OpenCV\\Phase4\\o.jpg", cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(image, 50,150)       #if (10,30) >>> detects many edges , cause too much noise
                                        #if (200, 300) >>> very clean but misses important edges
cv2.imshow("original", image)
cv2.imshow("Canny Edge", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
