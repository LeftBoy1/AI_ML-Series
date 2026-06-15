# ADDING 2 ARRAYS

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

sum = arr1 + arr2
print(sum)

combine = np.concatenate((arr1, arr2))  # concatenate() is used to join multiple NumPy arrays into one along a specified axis.
print(combine)






#DELETING 1D

import numpy as np

a = np.array([10, 20, 30, 40, 50])

b = np.delete(a, 2)   #2D_array , index
print(b)

c = np.delete(a, [1, 3])
print(c)




# DELETING 2D
import numpy as np
a = np.array([[1, 2],
              [3, 4],
              [5, 6]])

np.delete(a, 1, axis=0)   # 2D_array, index , axis=0 (remove row) 
print(a)
np.delete(a, 0, axis=1)   # 2D_array, index ,axis=1 (remove column)
print(a)





# Remove elements using a condition

import numpy as np
a = np.array([10, 20, 30, 40, 50])

a[a != 30]
print(a)






#Remove NAN values
import numpy as np
a = np.array([1, 2, np.nan, 4])

a[~np.isnan(a)]
print(a)