from numpy import *

arr=array([
    [1,2,3],
    [4,5,6],
    [6,6,7]
])

print(arr)

print(arr.ndim) # dimension
print(arr.shape) # type 3x3
print(arr.size)   # no of elements in matrix

print(arr.flatten()) # covert in one dimension array
x=arr.flatten()
print(x.ndim)

z=array([1,2,3,4,5,6,7,8,9,10,11,12])
print(z)

print(z.reshape(4,3))
print("3-d array")
print(z.reshape(2,2,3))