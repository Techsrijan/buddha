a=int(input("enetr first number"))
b=int(input("enter second number"))
c=int(input("Enetr third number"))

if a>b:
    if a>c:
        print("a is greatest")
    else:
        print("c is greatest")
elif b>c:
    print("b is greatest")
else:
    print("c is greatest")