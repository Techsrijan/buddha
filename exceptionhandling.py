try:
    print("fridge is open")
    a = int(input("enetr first number"))
    b = int(input("enter second number"))
    d=a/b
    print("division=",d)

except ValueError as e:
    print("You have entered a character not a number")

except ZeroDivisionError as e:
    print("b cant be zero")
except Exception as e:
    print("somthing went wrong")
finally:
    print("fridge is closed")

