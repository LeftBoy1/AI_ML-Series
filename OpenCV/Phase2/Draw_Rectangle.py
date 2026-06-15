import cv2

img = cv2.imread("F:\\Devansh_Gupta\\AI + ML\\OpenCV\\Phase 1\\o.jpg")

# cv2.rectangle(img, pt1, pt2, color, thickness)

pt1 = (490, 400)
pt2 = (710, 700)
color = (0,0 ,255)      #(blue, green, red)
cv2.rectangle(img, pt1, pt2, color, 5)


cv2.imshow("Rectangle",img)
cv2.waitKey(0)
cv2.destroyAllWindows()