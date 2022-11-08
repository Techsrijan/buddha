'''
Deriving a new class from the base class is known as inheritance.
types of inheritance
1. single level inheritance
2. multilevel inheritance
3. hierarchical inheritance
4. multiple inheritance
5. hybrib inheritance
'''
class Room:
    def area(self,l,b):
        self.l=l
        self.b=b
        area=self.l*self.b
        print("Area=",area)

class GuestRoom(Room):
    def msg(self):
        print("Guest Room")


r=Room()
r.area(40,50)

g=GuestRoom()
g.area(66,50)
g.msg()