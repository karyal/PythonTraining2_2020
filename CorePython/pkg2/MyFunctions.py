# Creating a Function

# No Parameter-No Return Type
def f1(): # No Parameter-No Return Type
    print("Hello from f1()")

# Parameterized - No Return Type
def f2(n1): # n1-> Parameter (which accept value from caller of function)
    print(n1)

# No Parameter - Return Type
def f3():
    tmp = int(input("Enter any number : ")) # Read value from Keyboard
    return (tmp)

# Parameterized - Return Type
def f4(n2):
    n2+=1
    return (n2)

# Keyword Parameter
def f5(num1, num2):
    print(num1+num2)

# Default Argumented
def f6(num1=0, num2=0):
    print(num1+num2)

# Recrusion
def f7(num1):
    if num1==1:
        return 1
    else:
        return num1+f7(num1-1)

# Nested Functions
def f8(num1):
    num1+=1
    f9(num1)

def f9(num1):
    num1 += 1
    f10(num1)

def f10(num1):
    num1 += 1
    print(num1)

# *args and **kwargs
# *args (Collections)
def f11(*nums):
    sum = 0
    for n in nums:
        sum+=n
    print(sum)

# **kwargs
def f12(**data):
    for key, value in data.items():
        print("{} = {} ".format(key, value))

# Lambda Function
f13 = lambda num1: num1*num1
print(f13(4))