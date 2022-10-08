from numpy import *
arr=array([1,2,3,4,6])
print(arr,id(arr))
print("aliasing ")
arr2=arr
print(arr2,id(arr2))

arr2[0]=5000
print(arr2,id(arr2))
print(arr,id(arr))
##############
print("view method--Shallow copy")
# what if u want two diffrent array ie address seprately

arr6=array([1,2,3,4,6])
print(arr6,id(arr6))

arr7=arr6.view()
print(arr7,id(arr7))

arr7[0]=67000
print(arr7,id(arr7))
print(arr6,id(arr6))


##############
print("Copy method--Deep Copy")
# what if u want two diffrent array ie address seprately changes of one does not affect other

arr3=array([1,2,3,4,6])
print(arr3,id(arr3))

arr4=arr3.copy()
print(arr4,id(arr4))

arr3[0]=1000
print(arr3,id(arr3))
print(arr4,id(arr4))
