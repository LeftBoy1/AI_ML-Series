import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.array([7,8,9])

print(f"Compatibility {a.shape == b.shape == c.shape}")




#ROW and COLUMN
import numpy as np

original = np.array([[1,2,3],[4,5,6]])


new_row = np.array([7,8,9])
adding_row = np.vstack((original,new_row))        #ye hmesha hi row add krta hai
print("New Row ", adding_row,"\n\n")


new_col = np.array([[7],[8]])
adding_col = np.hstack((original, new_col))         #ye hmesha hi column add krta hai
print("New Column ", adding_col,"\n\n")





#DELETING 
import numpy as np
arr1 = np.array([1,2,3,4,5])
new = np.delete(arr1 , 2)       #it DELETES element in array

print("Deleted Array ", new)