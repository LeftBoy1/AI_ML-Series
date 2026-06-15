'''Uses a Gaussian kernel (bell-shaped curve).
Each pixel is replaced by a weighted average of its neighbors.
Closer pixels have more influence than farther ones.

Effect on edges-
❌ Blurs edges
❌ Fine details may be lost'''

import cv2

# blurred_img = cv2.GaussianBlur(image, (kernel_size_x , kernel_size_y), sigma)

        #sigma = opacicty of blur
        
image = cv2.imread("F:\\Devansh_Gupta\\AI + ML\\OpenCV\\Phase4\\o.jpg")

blurred_img = cv2.GaussianBlur(image, (7,7), 2)

cv2.imshow("Original image", image)
cv2.imshow("Gaussian Blur", blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()