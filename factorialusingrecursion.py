def rec(n):
    if n==0:
        return 1
    f=n*rec(n-1)
    return f
print(rec(5))

