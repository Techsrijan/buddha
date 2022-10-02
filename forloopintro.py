'''
print(list(range(10)))
print(list(range(1,10)))
print(list(range(2,10,3)))

'''

for i in range(10):
    print(i)

for j in range(1,11):
    if j%2==0:
        print("even=",j)

l=[2,5,'xyz',3.2]
for k in l:
    print(k)

for m in range(len(l)):
    print(l[m])

i=0
while i<len(l):
    print(l[i])
    i=i+1