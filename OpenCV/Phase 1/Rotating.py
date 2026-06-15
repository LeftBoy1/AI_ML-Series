import cv2

img = cv2.imread("F:\\Devansh_Gupta\\AI + ML\\OpenCV\\o.jpg")

# M = cv2.getRotationMatrix2D(centre, angle, scale)
# rotated_img = cv2.warpAffine(img, M , (width, height))

    # cv2 = library
    # getRotationMatrix2D , warpfunction = function
    # rotated_img, M = variables
    # scale = scale or size of img(0.5, 1.0, 2.0)    
    
h,w = img.shape[:2]
centre = (w//2 , h//2)      #half of width and half of height

M = cv2.getRotationMatrix2D(centre, 45 , 1.0 )              #or       M = cv2.getRotationMatrix2D((w//2 , h//2), 45 , 1.0 )
rotated_img = cv2.warpAffine(img, M , (w, h))
    
cv2.imshow("Original", img)
cv2.imshow("Rotation", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()