import cv2

img = cv2.imread("F:\\Devansh_Gupta\\AI + ML\\OpenCV\\Phase 1\\o.jpg")

# cv2.putText(img, org, font, fontScale, color, thickness)
    # org = value of x,y    (org means “origin point” of the text. It defines where the text will start on the image.)
    

org = (600,350)
color = (0, 0, 255)


cv2.putText(img , "Hello", org, cv2.FONT_HERSHEY_DUPLEX, 2, color, 6)

cv2.imshow("Text", img)
cv2.waitKey(0)
cv2.destroyAllWindows()