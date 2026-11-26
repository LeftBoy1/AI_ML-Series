'''
Gaussian Blur is an image-smoothing technique that reduces noise and details by applying a Gaussian-weighted average to neighbouring pixels.
In simple words, it makes an image look blurry or smooth.
'''

# Kernel size controls the neighbourhood used for processing, and different sizes produce different levels of effect.
import cv2

# blurred_img = cv2.GaussianBlur(image, (kernel_size_x , kernel_size_y), sigma)

        #sigma = opacicty of blur
        
image = cv2.imread("D:\\Devansh_Gupta\\AI + ML\\OpenCV\\Phase4\\o.jpg")

blurred_img = cv2.GaussianBlur(image, (7,7), 2)

cv2.imshow("Original image", image)
cv2.imshow("Gaussian Blur", blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()