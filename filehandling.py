f=open("hello.txt","r")
print(f)
#print(f.read()) #whole content of file
#print(f.read(5))  #only display no of characters
#print(f.readline()) # display only one line
#print(f.readline())
#print(f.readlines()) # list

for data in f:
    print(data)