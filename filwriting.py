#f=open("hello.txt","w")
f=open("hello.txt","a")
w=input("enter the contennts u want to store in a file")
f.write(w)
f.close()


f1=open("hello.txt","r")
print(f1.read())