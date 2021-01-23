# Syntax Error
"""
# ----------------------------------------
while True print('Hello world')

# Output
while True print('Hello world')
                   ^
SyntaxError: invalid syntax

# ----------------------------------------
10 * (1/0)

# Output
10 * (1/0)
ZeroDivisionError: division by zero

# ----------------------------------------

4 + var1 *3

# Output
4 + var1 *3
NameError: name 'var1' is not defined

# ----------------------------------------
'2' + 2

# Output
'2' + 2
TypeError: can only concatenate str (not "int") to str


# Handling Exception
import sys
list1 = [10, 2, 'A']
try:
    for item in list1:
        print(item)
        result = 1/int(item)
except:
    #print("Error : ", sys.exc_info())
    print("Error : ", sys.exc_info()[0])

# Error :  <class 'ZeroDivisionError'>
# Error :  <class 'ValueError'>


# Handling Mutiple Exceptions
import sys
list1 = [10, 0, 'A']
try:
    for item in list1:
        print(item)
        result = 1/int(item)
except ZeroDivisionError:
    print("Error : ", sys.exc_info()[0])
except ValueError:
    print("Error : ", sys.exc_info()[0])
except:
    print("Error : ", sys.exc_info()[0])

# Handling Multiple Exceptions
import sys
list1 = [10, 2, 'A']
try:
    for item in list1:
        print(item)
        result = 1/int(item)
except (ZeroDivisionError, ValueError):
    print("Error : ", sys.exc_info()[0])


# Try, Except and Finally
import sys
try:
    n1 = int(input("Enter first no : "))
    n2 = int(input("Enter first no : "))
    n3 = n1 / n2
    print("Result : ", n3)
except (ValueError, ZeroDivisionError):
    print("Error : ", sys.exc_info()[0])
finally:
    del n1
    del n2
    del n3


class MyError(Exception):
    pass

class ValueToSamllError(MyError):
    pass

class ValueToLargeError(MyError):
    pass

num1 = 10
while True:
    try:
        tmp_num = int(input("Enter any number : "))
        if tmp_num<num1:
            raise ValueToSamllError
        elif tmp_num>num1:
            raise ValueToLargeError
        print(tmp_num, " Value is in range")
        break
    except ValueToSamllError:
        print("Value is to samll!")
    except ValueToLargeError:
        print("Value is to large!")
    finally:
        del tmp_num
"""