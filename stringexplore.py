str1="welcome in Python"
print(str1)
print(len(str1))
print(str1.capitalize())
print(str1.upper())
print(str1.lower())
print(str1.title())
print(str1.swapcase())

'''
name=input("enetr ur name")
if name.isalpha():
    print(name.upper())
else:
    print("not valid name")


print(name.isupper())

age=input("enetr ur age")
if age.isdigit():
    print(age)
else:
    print("not valid age")

empid=input("enetr ur empid")
if empid.isalnum():
    print(empid)
else:
    print("not valid ")



name=input("enter us name")
print(name.strip('!'),end="")   
print("Thank you")
'''

#lstrip rstrip
str3="her name is tamanna and tamanna is good girl"
search="tamanna"
print(str3.find(search))
rep="Sonia"
if str3.find(search):
    print(str3.replace(search,rep))

print(str3.index(search))


print(str3.endswith('m'))

print(str3.split(' '))

l=eval(input("Enter the element of list"))
print(l)
print(type(l))