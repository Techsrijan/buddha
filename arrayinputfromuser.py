from array import *
arr=array('i',[]) #empty array
n=int(input("how many elements u want to store in an array"))
for i in range(n):
    x=int(input("enetr the elements"))
    arr.append(x)

for i in arr:
    #time.sleep(1)
    print(i)

loc=0
search=int(input("Which element u want to search"))
for i in arr:
    if i==search:
        print("Item Found=",loc)
        break
    loc=loc+1
else:
    print("Item Not found")

# this is python function to search
result=arr.index(search)
print(result)