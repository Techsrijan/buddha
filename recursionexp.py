'''
when a function calls itself it is called recursion
'''
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(sys.getrecursionlimit()+5000)
print(sys.getrecursionlimit())

def greet():
    global i
    print("Good morning=",i)
    i=i+1
    greet()
i=1
greet()