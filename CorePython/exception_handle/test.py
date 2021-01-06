# Exception Handles
"""
1. NameError
2. SyntaxError
3. ZeroDivisionError
4. TypeError

Hello="Hi"
print(Hello) # NameError: name 'Hello' is not defined

while True print("Hi") # SyntaxError: invalid syntax

while True:
    print("Hi")

res = 10/0 # ZeroDivisionError: division by zero
print(res)

res = 1+'2' # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(res)

str1 ="123.258"
num1 = int(str1) # ValueError: invalid literal for int() with base 10: '123.258'
print(num1)

# How to handle runtime errors in python
import sys
str1=None
num1=None
try:
    str1 = input("Enter any number : ")
    num1 = int(str1) # ValueError: invalid literal for int() with base 10: '123.258'
    print(num1)
except:
    print("Error : ", sys.exc_info()[1])
finally:
    del str1
    del num1
"""

# Example-2
import sys
# Declare variable
num1 = None
num2 = None
num3 = None
try:
    # input, process, output
    tmp = input("Enter first no : ")
    tmp2 = input("Enter second no : ")
    num1 = float(tmp)
    num2 = float(tmp2)
    num3 = num1/num2
    print("Resutl : ", num3)
except:
    # print error message
    print("Error : ", sys.exc_info()[1])
finally:
    # free memory
    del num1
    del num2
    del num3

# HW Jan 5, 2021
# 1. How to handle multiple errors
import sys
# declare
list1 = [1, 7, 2, 6, 5]
num1 = 5
try:
    print("Result 1 : ", list1[4]) # Error :  list index out of range
    print("Result 2 : ", list1[3]/num1) # Error :  division by zero
except IndexError:
    print("Error1 : ", sys.exc_info()[1])
except ZeroDivisionError:
    print("Error2 : ", sys.exc_info()[1])
except:
    print("Error3 : ", sys.exc_info()[1])
finally:
    del num1
    del list1

# User defined errors - handling
class MyException(Exception):
    pass
# Create User Defined Class MyError which is inherited from Exception Class(System Defined Class)

class ValueToSamllException(MyException):
    pass

class ValueToLargeException(MyException):
    pass

# Test program which test the user defined exceptions
num1 = 7
try:
    if num1>10:
        raise ValueToLargeException
    elif num1<5:
        raise ValueToSamllException
    else:
        print("Num1 =", num1)
except ValueToLargeException:
    print("Error: Value to large in range.")
except ValueToSamllException:
    print("Error: Value to small in range.")
finally:
    del num1