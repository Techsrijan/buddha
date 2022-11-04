class Student:
    def getData(self,name,age):
        self.name=name
        self.age=age

    def putData(self):
        print("name=",self.name)
        print("age=",self.age)

    def addDatamain(self):
        pass

    def addData(self,x,y):
        self.x=x
        self.y=y

    def add(self):
        print(self.x+self.y)
    #constructor
    def __init__(self):
        self.x = 0
        self.y = 0
        print("lo mein aaga gaya")

s=Student() #object creation
s.getData("Rohan",40)
s.putData()
# Student.getData(s,"Rohan",40)
# Student.putData(s)
#s.addDatamain()
#s.addData(5,6)
s.add()

'''
constructor is a special member function which invoked(call)
automaitcally when the object is created
'''
s2=Student()
s2.add()