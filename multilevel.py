class Student:
    def student_info(self):
        print("Hum don hi")

class Marks(Student):
    def getMarks(self):
        print("Don ka marks hi")

class Result(Marks):
    def result(self):
        print("Result kiska hi")

        
s=Result()
s.student_info()
s.getMarks()
s.result()