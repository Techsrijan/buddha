f=open("hello.txt","r")
f1=open("hellocopy.txt","a")

for data in f:
    f1.write(data) 