# 1. Create different rows
import numpy as np

row1 = np.full(4, 1)
row2 = np.full(4, 2)
row3 = np.full(4, 3)

matrix = np.vstack([row1, row2, row3])  #np.vstack() is used to stack arrays vertically (row-wise).
print(matrix)






# 2. Fill columns differently
import numpy as np

col1 = np.full(3, 1)
col2 = np.full(3, 2)
col3 = np.full(3, 3)

matrix = np.column_stack([col1, col2, col3])
print(matrix)









# 3. Start with np.full() then modify values
import numpy as np

matrix = np.full((3, 3), 0)

matrix[0] = 1       
matrix[1] = 5        
matrix[2, 2] = 9     
print(matrix)








# 4. If you want different values per cell
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr)






# 5. Using arange() function
import numpy as np
x = np.arange(1, 10).reshape(3,3)
print(x)