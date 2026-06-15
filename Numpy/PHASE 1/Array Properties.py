import numpy as np

arr = np.array([[2,3,4],
        [1,2,3]])
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Dimension:", arr.ndim,"D")
print("Data Type:", arr.dtype)



# Reshape, Flatten, Ravel, Transpose,
import numpy as np
arr1 = np.arange(12)     #starts from 0 to 11
print(f"Original Array:-\n{arr1}\n")



#Reshaping
reshaped = arr1.reshape((3,4))
print(f"Reshaped Array:-\n{reshaped}\n")




#Flating
flating = reshaped.flatten()                    #It converts a multi-dimensional array (2D, 3D, …) into a 1D array.
print(f"Flattend Array:{flating}\n")




#Ravel                           
raveled = reshaped.ravel()        #It also converts a multi-dimensional array (2D, 3D, …) into a 1D array.
print(f"Raveled Array:{raveled}\n")



#Transpose
transpose = reshaped.T
print(f"Transposed Array:\n{transpose}\n")




'''Difference between Flatten() and Ravel()

1. Ravel - Returns a view (no new memory, faster)   ,   Changing it may change the original array

        
2. Flatten - Returns a copy (uses extra memory)  ,   Original array stays safe



EXAMPLE -
import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a)

b = a.ravel()
b[0] = 99
print(b)

c = a.flatten()
c[1] = 88
print(c)



OUTPUT - 
[[1 2] 
 [3 4]]
[99  2  3  4]
[99 88  3  4]

'''