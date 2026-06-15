# Filtering in NumPy is used to select or remove elements based on a condition.

import numpy as np

num = np.array([1,2,3,4,5,6,7,8,9,10])
even_num = num[num % 2 == 0]
print(even_num, "\n")



#Filtering with Mask
import numpy as np

num = np.array([1,2,3,4,5,6,7,8,9,10])
mask = num > 5

print(f"{num[mask]}\n\n")
print(f"{mask}\n")