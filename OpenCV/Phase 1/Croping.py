import cv2

img = cv2.imread("F:\\Devansh_Gupta\\AI + ML\\OpenCV\\o.jpg")

# crop = img[start[y]:end[y] , start[x]:end[x]]
  
crop = img[490:890, 910:2110]


cv2.imshow("Original_Image", img)
cv2.imshow("Cropped_Image", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()