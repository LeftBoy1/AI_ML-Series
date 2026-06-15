import cv2

img = cv2.imread(r"F:\Devansh_Gupta\AI + ML\OpenCV\Phase 1\o.jpg")

# resize = cv2.resize(src, dsize, fx, fy, interpolation)
    # src = image file
    # dsize = size of image (width, height)
    # fx and fy = scale factors (optional)
    # interpolation = used to make more clear/precise image
    
if img is None:
    print("Image Not Found")
    
else:
    resized = cv2.resize(img, (600, 300))
    print("Image Loaded Successfully")
    
    cv2.imshow("Original", img)
    cv2.imshow("Resized", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    