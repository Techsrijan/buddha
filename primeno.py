'''n=999
i=2
while i<=n-1:
    if n%i==0:
        print("Not Prime")
        break
    i=i+1
else:
    print("Prime")

'''
n=2
while n<=20:
     #print(n)
     i=2
     while i <= n - 1:
         if n % i == 0:
             #print("Not Prime=",n)
             break
         i = i + 1
     else:
         print("Prime=",n)
     n=n+1