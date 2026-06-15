#Numpy from Scratch

# matrix = np.full((3, 3), values)

import numpy as np
x = np.full((300,300),7)
print(x)
zero = np.zeros((3,3))
print(zero,"\n")

one = np.ones((3,3))
print(one,"\n")

full = np.full((3,3),7)
print(full,"\n")





'''
np.random.rand() - You pass shape directly as arguments
    Example - np.random.rand(3, 2)
    
np.random.random() - You pass shape as a tuple
    Example - np.random.random((3, 2))
'''
random = np.random.random((3,3))
print(random,"\n")

# random() with desired range
low, high = 5, 10
x = low + (high - low) * np.random.rand()
print(x)




sequence = np.arange(0,11,2)        #np.arange(start, stop, step)
print(sequence,"\n")