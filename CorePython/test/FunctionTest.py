"""
from pkg2.MyFunctions import f1
from pkg2.MyFunctions import f2
from pkg2.MyFunctions import f3
from pkg2.MyFunctions import f4
from pkg2.MyFunctions import f5
from pkg2.MyFunctions import f6
"""

from pkg2.MyFunctions import *

"""
# Function Call
f1()  # Function Call

# Function Call-2
num1 = 90
f2(num1)# Passing value to f2 function as argument

# Function Call-3
num2 = f3() # Call f3() and return value to assign on num2
print(num2)

#Function Call-4
num3 = f4(47)
print(num3)

# Keyword Parameter # def f5(num1, num2):
f5(num2=2, num1=5)
f5(num1=10, num2=3)
f5(2, 5)

# Default Parameter
f6(num2=9)

# Recrusion
result = f7(5)
f2(result)

# Nested Functions
f8(5)

f11(3,4,5,6,7,8,9,0,12,2,3)
"""

f12(pid=1, name="Krishna", address="Kalanki")
f12(pid=2, name="Kiran")

# Lambda function
f13 = lambda num1: num1*num1

print(f13(4))