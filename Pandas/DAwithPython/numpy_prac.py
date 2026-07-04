import numpy as np

# create array with numpy
# 1D array
arr1 = np.array([1,2,3])
print(arr1)
print(arr1.shape)
print(type(arr1))

arr2 = np.array([[1,2,3,20] ,[4,5,6,20],[7,8,9,20]])
print(arr2)
print(arr2.shape)

arran = np.arange(1,10,2)
print(arran)

one = np.ones([4,5])
print(one)

# vectorized operations
arr3 = np.array([19,20,21])
print(f"Addition:{arr1+arr3}")

# universal functions
print(np.sqrt(arr1))
print(np.exp(arr1))

# array slicing and indexing

arr2 = np.array([[1,2,3,20] ,[4,5,6,20],[7,8,9,20]])

print(arr2)
print(arr2[0][3])
print(arr2[0:,3:])

print(arr2[0:2,2:])

# 5,6,8,9
print(arr2[1:,1:3])

