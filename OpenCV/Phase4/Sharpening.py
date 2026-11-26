'''
harpening is an image-processing technique that enhances edges and fine details to make an image appear clearer and more defined.
In simple words, it makes an image look sharper rather than blurry.
'''
import cv2
import numpy as np

# cv2.filter2D(src, ddepth, kernel)

'''
    ddepth means Destination Depth.
    It defines the data type (bit depth) of the output image after applying a filter (like sharpening).
    In simple words:
            ddepth decides how pixel values will be stored in the resulting image.
    '''
image = cv2.imread("D:\\Devansh_Gupta\\AI + ML\\OpenCV\\Phase4\\o.jpg")

sharpen_kernel = np.array([
    [0 , -1 , 0],
    [-1 , 5 ,-1],
    [0 , -1 , 0],
])

sharpen = cv2.filter2D(image , -1, sharpen_kernel)      #depth= -1 , gives output same as input's depth

cv2.imshow("Sharpen", sharpen)
cv2.imshow("Original image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()