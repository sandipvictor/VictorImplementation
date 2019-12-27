''' error:-> Compile time error, eg -> Syntax error
            logical error, eg -> out put is not coming as expected , like 2+2 =5
            Runtime error, eg -> error come at run time because user did not give correct input, like 2/0
'''

# error handling ***********



try:
    print("open")
    a = int(input(" user enter the  for a"))
    b = int(input("2nd user enter the number for b"))
    x = a / b
    print(" division of", a, b, "is", x)
except ValueError as v:
    print("Invalid Input", v)
except ZeroDivisionError as z:
    print("Hey you can not divide by zero", z)
except Exception as e:
    print(" Something went wrong",e)

finally:
    print(" close the operation")
