stock=15
n=int(input("how many toffee you want"))
i=1
while i<=n:
    if i<=stock:
        print("Collect Toffe=",i)

    else:
        print("Out Of stock")
        break
    i=i+1
else:  # when the loop runs properly
    print("thank you Please visit again")