f=0
s=1
print(f,",",s,end="")
for i in range(10):
    t=f+s
    print(",",t,end="")
    f=s
    s=t
