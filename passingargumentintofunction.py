def person(name,age):
    print(name)
    age=age+10
    print(age)


'''
There are 4 ays to pass argument into function
1. positional argument
2. keyword argument
3. varaible length argument
4. keyword varaible length argument
'''
# positional argument
person("Rohan",56)
#keyword argument
person(age=63,name="Shivam")

def add(x,y,z):
    c=x+y+z
    print(c)

add(4,6,7)
#varaible length argument
def varsum(x,*y):
    print(x)
    print(y)
    sum=x
    for i in y:
        sum=sum+i
    print(sum)


varsum(5,6,8,7.9)


def varsum1(*x):
    print(x)
    sum=0
    for i in x:
        sum=sum+i
    return sum


t=varsum1(5,6,8,7.9)
print(t)

#keyword varaible length argument
def persondata(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,"=",j)

persondata(name="Rohasn",age=25,city='gkp',mob='9956477677',school='mg')
