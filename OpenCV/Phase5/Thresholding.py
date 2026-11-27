# cv2.threshold() works on a single-channel image, not on a 3-channel color image.
import cv2
# thresholding_img = cv2.thresholding(image, thresh_value, max_value ,method)
        #thresh_value = (0,255)
        #max value = 255
        #method = THRESH BINARY    (sets img into black(0) or white(255))
#we use threshold ,To separate important objects from the background        

image = cv2.imread("D:\\Devansh_Gupta\\AI + ML\\OpenCV\\Phase4\\o.jpg", cv2.IMREAD_GRAYSCALE)

ret, thresh =  cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)        #ret stores the threshold value returned by the cv2.threshold() function where thresh shows the image

cv2.imshow("Original Image", image)
cv2.imshow("Threshold Image", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()


''' less then 120 = changes to black
    greater then 120 = changes to white'''