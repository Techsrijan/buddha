x=50

def test():
    global y
    #y=500
    x=5
    print("local=",x)
    d=globals()['x']
    print("Global but print local=",d)

y=500
def best():
    pass

test()
print("global=",x)
print("local global=",y)