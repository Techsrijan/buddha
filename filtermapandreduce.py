from functools import *
l=[4,58,33,77,92,36,11,2566,445,66,4,3,2,8]
y=lambda n:n%2==0
op=list(filter(y,l))
print(op)
f=lambda a:a+10
map_result=list(map(f,op))
print(map_result)

t=lambda a,b:a+b
final_value=reduce(t,map_result)
print(final_value)