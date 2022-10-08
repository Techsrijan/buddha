from numpy import *

'''
arr=array([1,2.0,3,4,6])
print(arr)

for i in arr:
    print(i)


There are six ways to create an array using numpy
1. array()
2. linspace
3. logspace
4. arange
5. zeros
6. ones
'''

arr1=linspace(1,15)
print(arr1)

arr2=logspace(1,15)
print(arr2)

arr3=arange(1,15,2)
print(arr3)

arr4=ones(110,int)
print(arr4)

arr5=zeros(10,int)
print(arr5)

arr5=zeros(10)
print(arr5)