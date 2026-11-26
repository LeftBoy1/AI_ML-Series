'''
Median Blur is a noise-removal technique that replaces each pixel with the median value of its neighbouring pixels.
In simple words, it looks at surrounding pixels, sorts their values and replaces the centre pixel with the middle value.
'''
import cv2

# blurred = cv2.medianBlur(image, kernel_size)

image = cv2.imread("D:\\Devansh_Gupta\\AI + ML\\OpenCV\\Phase4\\o.jpg")
blurred = cv2.medianBlur(image, 5)

cv2.imshow("Median Blur", blurred)
cv2.imshow("Original", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
