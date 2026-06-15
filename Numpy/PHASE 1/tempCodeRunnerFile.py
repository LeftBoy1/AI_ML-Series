import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a)

b = a.ravel()
b[0] = 99
print(b)

c = a.flatten()
c[1] = 88
print(c)