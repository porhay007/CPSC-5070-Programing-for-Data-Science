#NumPy Arrays
# 1 What's NumPy and why numpy arrays?
# 2. Creating arrays from python lists(or other iterables)
# 3 Creating arrays using built-in methods (quite a few!)
# 4. Shape and Reshape


a = [1,2,3,4,5,6]

print(type(a))

import numpy as np

print(set(a))
 
#numpy array
print(np.array(a))

print(type(np.array(a)))

# Two dimensional array or Matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix)

print(np.array(matrix))

print(np.array((1,2,3,4,5)))

print(np.array(range(10)))

print(np.array(range(1,10,2)))

print(np.array({1,2,3}))

print(np.array(list({1,2,3})))
