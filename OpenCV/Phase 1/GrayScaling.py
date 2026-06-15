import cv2

img = cv2.imread(r"F:\Devansh_Gupta\AI + ML\OpenCV\Phase 1\o.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)       #changes color of img to another color, like - gray&white

cv2.imshow("GrayScaling Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()