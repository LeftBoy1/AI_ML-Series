import numpy as np
#BASIC NUMPY ARRAY-

arr1 = np.array([1,3,4])
arr2 = np.array([[2,4,6], [4,9,6]])

print(arr1)
print(arr2)


#PY VS NP ARRAY-

    #PY
import numpy as np
py_array = [1,2,3]
print(py_array*2)

    #NP
np_array = np.array([1,3,5])
print(np_array*2)




    #PY
import time
start = time.time()
py_list = [i*2 for i in range(1000)]
print(py_list)
print("\n",time.time()- start)
    
    #NP
import numpy as np
import time
start = time.time()
np_array = np.arange(1000)/2           # starts from 0 to 999 and gets multiple by 2
print(np_array)
print("\n",time.time()- start,"\n")


'''
np.arange() - Creating an array with evenly spaced values within a given range, similar to Python’s range() but it returns a NumPy array.
        SYNTAX - 
                    numpy.arange(start, stop, step)
'''