def add(x,y):
   return x+y

print(add(3,4))


def is_even(n):
    return n%2==0
'''
the above fuction can be made anonymous
because it have only one statement 
for this we need lambda function

A lambda function can take any number of arguments, but can only have one expression.
'''
y=lambda n:n%2==0
f=lambda a,b:a+b

print(f(6,7))

print(y(50))

