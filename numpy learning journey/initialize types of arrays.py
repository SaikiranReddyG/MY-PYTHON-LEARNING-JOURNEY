import numpy as np
# all 0s matrix
a = np.zeros(5)
print(a)
b = np.zeros((2, 3))
print(b)
c = np.zeros((2, 3, 3, 4))
print(c)

# all 1s matrix
d = np.ones((4, 2, 2))
print(d)

# any other number
e = np.full((2, 2), 9999)
print(e)

# full like method
r = np.full_like(e, 4)
print(r)

# random decimal numbers
import random
t = np.random.rand(4, 2)
print(t)
w = np.random.random_sample(e.shape)
print('the ans is', w)


# random decimal numbers
u = np.random.randint(4, size=(3,3))
print('u is', u)

# identity
p = np.identity(5)
print(p)

# repeat
ar = np.array([1,2,3])
rr = np.repeat(ar, 3)
print(rr)

ss = np.array([1, 2, 3])
ee = np.repeat(ss, 3, axis=0)
print(ee)

# 2d repeat
sse = np.array([[1, 2, 3]])
ees = np.repeat(sse, 3, axis=0)
print(ees)

# initialize an example
"""a matrix with all ones"""
output = np.ones((5, 5))
print(output)
"""a matrix with all zeroes"""
z = np.zeros((3,3))
print(z)
"""change the middle of z to 9"""
z[1,1] = 9
print(z)
"""now insert z into output"""
output[1:4, 1:4] = z
print(output)