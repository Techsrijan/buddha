from array import *
import time
l=array('f',[1,2,3,4,6.0,66,44,77])
print(l)

for i in l:
    #time.sleep(1)
    print(i)

for j in range(len(l)):
    print(l[j])

print(l.buffer_info())

