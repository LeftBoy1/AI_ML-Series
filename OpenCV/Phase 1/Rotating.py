import cv2

img = cv2.imread(r"D:\Devansh_Gupta\AI + ML\OpenCV\Phase 1\o.jpg")

# M = cv2.getRotationMatrix2D(centre, angle, scale)
# rotated_img = cv2.warpAffine(img, M , (width, height))

    # cv2 = library
    # getRotationMatrix2D , warpfunction = function
    # rotated_img, M = variables
    # scale = scale or size of img(0.5, 1.0, 2.0)    
    
h,w = img.shape[:2]
centre = (w//2 , h//2)      #half of width and half of height

M = cv2.getRotationMatrix2D(centre, 45 , 1.0 )
rotated_img = cv2.warpAffine(img, M , (w, h))       
    
cv2.imshow("Original", img)
cv2.imshow("Rotation", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
cv2.warpAffine() is an OpenCV function used to transform an image, such as rotating, shifting (translating), resizing or applying certain geometric transformations.

cv2.warpAffine() cannot understand by itself how much to rotate an image, where to rotate it, or what scale to use.
That's why we use cv2.getRotationMatrix2D() first.

'''