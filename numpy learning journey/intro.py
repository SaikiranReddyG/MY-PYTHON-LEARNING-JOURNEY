"""numpy is a multi dimensional array library
   i.e we can use numpy to store all kinds of data such as 1d, 2d, 3d, arrays"""

"""numpy is used over lists bcoz 
   1>> fast 
   2> numpy uses fixed types i.e
   the binary data of a integer is convered to 32bit, 16bit, or 8bit
   with put no extra information byt  alist has different info for each integer
   like obj type value size refer count 
   3>> when iterating in loops you dont have to check type 
   for each iteration as donr in lists
   4>> numpy uses contiguous memory, i.e all blocks of data as sise by side to each other
    so it will be easy to access
    5>> we can do all things a list does , like i nsertion, deletion, appending, concatenation
    and many things list does not do"""
# example
import numpy as np
# a = [1, 3, 5]
# b = [1, 2, 3]
# print(a*b)
"""it is not possible with normal lists, to multiply a & b """
a = np.array([1, 3, 5])
b = np.array([1, 2, 3])
print(a*b)

# applicatons of numpy
"""mathematics  (MATLAB replacement)
   plotting(Matplotlib)
   backend(pandas, connect4, digital photography)
   machine-learning"""
