#Fancy Indexing vs  np.where()
import numpy as np

num = np.array([1,2,3,4,5,6,7,8,9,10])
indices = [0,2,4,9]
print(num[indices])

where_result = np.where(num > 5)
print(num[where_result])    

condition_arr = np.where( num>5 , "True", "False")
print(condition_arr)
  
            #OR

# if num > 5:
#     print("True")
# else:
#     print("False")
