import cv2

img = cv2.imread(r"F:\Devansh_Gupta\AI + ML\OpenCV\Phase 1\o.jpg")

# variable = cv2.flip(img, value)   
    # value = 1 >>>> Horizontal
    # value = 0 >>>> Vertical
    # value = -1 >>>> Both Vertical and Horizontal
    
    
    
    
flipped_vertical = cv2.flip(img, 0)
flipped_horizontal = cv2.flip(img, 1)
flipped_both = cv2.flip(img, -1)

cv2.imshow("Flipped_Both", flipped_both)
cv2.imshow("Flipped_Horizontal", flipped_horizontal)
cv2.imshow("Flipped_Vertical", flipped_vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()