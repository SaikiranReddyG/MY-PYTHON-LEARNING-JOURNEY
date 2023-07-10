import numpy as np
a = np.array([1, 2, 3])
print(a)

# 2d arrays
b = np.array([[9, 0, 8, 0, 7, 0], [6, 0, 5, 0, 4, 0]])
print(b)

# get dimensions of array
print(a.ndim)
print(b.ndim)

# get shape  (matrix form)
print(a.shape)
print(b.shape)

# get type
print(a.dtype)
print(b.dtype)

# get size
print(a.itemsize)
print(b.itemsize)

# get total size
print(a.size * a.itemsize)
"""or"""
print(a.nbytes)
