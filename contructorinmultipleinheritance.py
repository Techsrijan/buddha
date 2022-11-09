class A:
    def __init__(self):
        print("Class a constr")

class B:
    pass
    # def __init__(self):
    #     print("Class b constr")
class C(B,A):
    pass

c=C()
