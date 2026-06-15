'''Replaces each pixel with the median value of neighboring pixels.
Not an average → outliers are ignored

Effect on edges-
✅ Preserves edges better
✅ Keeps sharp boundaries'''



'''
    In median blur, the kernel size defines the size of the neighborhood around each pixel that OpenCV looks at to decide the new pixel value.
        Example - cv2.medianBlur(img, 5)
                    So, 
                    What actually happens (step-by-step)

                        For every pixel:
                        1.Take a 5×5 block of pixels around it
                        2.Collect all their intensity values
                        3.Sort them
                        4.Pick the middle (median) value
                        5.Replace the center pixel with that value
                        👉 No averaging, only the median'''
import cv2

# blurred = cv2.medianBlur(image, kernel_size)

image = cv2.imread("F:\\Devansh_Gupta\\AI + ML\\OpenCV\\Phase4\\o.jpg")
blurred = cv2.medianBlur(image, 5)

cv2.imshow("Median Blur", blurred)
cv2.imshow("Original", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
