import  numpy as np
a = np.array([[1,2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)

# get a specific element
"""get an element of 1st row and 5th coulmn """
print(a[1, 5])

# get specific row
print(a[0, :])

# get specific coulmn
print(a[:, 2])

# more fancy [startindex, endindex, stepsize]
print(a[0, 1:6])
print(a[0, 1:-1:-2])

# change an element
a[1, 5] = 55
print(a)
a[:,2] = [1, 2]
print(a)

# 3d array
b = np.array([[[1,2], [3, 4]], [[5, 6], [7, 8]]])
print(b)

# get specific element (work outside in)
print(b[0, 1, 1])
print(b[:, 0, :])

# replace
b[:, 1, :] = [[9, 9], [8, 8]]
print(b)


