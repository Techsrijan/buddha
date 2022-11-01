f=open("test.gif","rb")
f2=open("best.gif","wb")
#print(f.read())
for data in f:
    f2.write(data)