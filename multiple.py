class Theory:
    def get_theory_marks(self):
        print("Theory markks")

class Practical:
    def get_priacical_marks(self):
        print("priacical markks")

class Result(Theory,Practical):
    pass

s=Result()
s.get_theory_marks()
s.get_priacical_marks()