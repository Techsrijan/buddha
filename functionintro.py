from math import *
#function definition

def greet():
    print("Good Morning")

greet() # function call
greet()
print("Deckho kaise run hota hi function")
greet()
greet()


#function which takes  no argument or parameter
def add():
    #a,b=5,6
    a=int(input("enetr first number"))
    b = int(input("enetr second number"))
    c=a+b
    print(c)

#add()
#add()

#function which takes argument or parameter
def sub(x,y):  #here x and y are called formal argumnet
    d=x-y
    print(d)


a=int(input("enetr first number"))
b = int(input("enetr second number"))
sub(a,b) # here a and b are actual argument


#function which takes argument or parameter and return a value
def mul(p,q):
    m=p*q
    return m

result=mul(8,9)
print("Result=",result)

x=sqrt(36)
print(x)





