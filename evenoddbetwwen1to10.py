
'''

i=200
while i<=400:
    if i % 2 == 0:
        print("even no=",i)
    else:
        print("odd no=",i)
    i=i+1
'''
count=0
kahase=int(input("eneter starting point"))

kahtak=int(input("eneter ending point"))
i=kahase
while i<=kahtak:
    if i % 2 == 0:
        print("even no=",i)
        count=count+1
    else:
        print("odd no=",i)
    i=i+1

print("no of even no=",count)