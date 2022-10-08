from numpy import *

arr=array([
    [1,2,3],
    [4,5,6],
    [6,6,7]
])

print(arr)


arr2=array([
    [1,2,3],
    [4,5,6],
    [6,6,7],

])

print(arr2)

c=arr+arr2
print(c)

print(diagonal(c))

print("multiply")
print(dot(arr,arr2))

print(arr@arr2)

print(sqrt(36))