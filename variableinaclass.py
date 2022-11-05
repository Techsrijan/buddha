'''
class variable --class
instance variable-method
'''

class Car:
    wheel=4  #class variable
    def car_info(self):
        self.name='Toyta'   #mil and name instance
        self.mil=15
        print(self.name)

c1=Car()
c1.car_info()
c2=Car()
c2.car_info()
c1.name="Maruti"
print(c1.name)
print(c2.name)
c1.car_info()
c2.car_info()
print(c1.wheel)
print(c2.wheel)
#c1.wheel=9
print(c1.wheel)
print(c2.wheel)
Car.wheel=50
print(c1.wheel)
print(c2.wheel)
Car
