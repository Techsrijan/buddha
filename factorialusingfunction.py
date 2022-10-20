'''
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(factorial(5))
'''
if __name__ == '__main__':
    numbers = [int(n) for n in input().split()]
    integer_list=tuple((numbers))
    print(integer_list)
    print(hash(integer_list))

print(__name__)


print("Enter the numbers: ")

inp = tuple(map(int, input().split()))

print(inp)
print(hash(inp))