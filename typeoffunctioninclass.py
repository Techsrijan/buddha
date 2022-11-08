'''
1. instance method --self
2. static method
3. class mtehod
'''

class Student:
    school="techsrijan"
    def getmarks(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def totalmarks(self):
        return self.m1+self.m2+self.m3

    @staticmethod
    def msg():
        print("Kaise Run Karoon mein ab")

    @classmethod
    def schoolname(cls):
        print(cls.school)


Student.msg()
s=Student()
s.getmarks(10,20,30)
print("Total=",s.totalmarks())
Student.schoolname()
