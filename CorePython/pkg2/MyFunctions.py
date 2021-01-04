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