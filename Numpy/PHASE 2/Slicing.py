import numpy as np

#1D Array
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print("Basic Slicing:", arr[2:7])
print("With Step:", arr[1:10:2])        #arr[start:end:gap]

#: = all rows or all columns

#2D Array
import numpy as np
arr1 = np.array([[2,3,4],   #0th row
                 [5,6,7],   #1st row
                 [1,2,3]])  #2nd row

print("Specific Element:",arr1[1,2])
print("Entire Row:",arr1[1])
print("Entire Column:",arr1[:,1])


#array[row_start:row_end, col_start:col_end]