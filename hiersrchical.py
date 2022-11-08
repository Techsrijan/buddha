class Account:
    def customer_info(self):
        print("Have customer data")

class Saving(Account):
    def s_interest(self):
        print("4%")

class Current(Account):
    def c_interest(self):
        print("no interest")

s=Saving()
s.customer_info()
s.s_interest()

c = Current()
c.customer_info()
c.c_interest()
