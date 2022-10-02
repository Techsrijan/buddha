n=153
o=n
sum=0
while n>0:
    a=n%10
    sum=sum+a*a*a
    n=n//10

print("sum=",sum)

if o==sum:
    print("armstrong no")
else:
    print("not armstrong")
