
import cv2

img = cv2.imread("D:\\Devansh_Gupta\\AI + ML\\OpenCV\\Phase4\\o.jpg")

blur1 = cv2.GaussianBlur(img, (3, 3), 0)
blur2 = cv2.GaussianBlur(img, (5, 5), 0)
blur3 = cv2.GaussianBlur(img, (9, 9), 0)

cv2.imshow("Original", img)
cv2.imshow("3x3", blur1)
cv2.imshow("5x5", blur2)
cv2.imshow("9x9", blur3)

cv2.waitKey(0)
cv2.destroyAllWindows()