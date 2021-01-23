# if statement
num1 = 5
if num1 == 0:
    print("Zero")

if num1 == 1:
    print("One")

if num1 == 2:
    print("Two")

if num1 == 3:
    print("Two")

if num1 == 4:
    print("Four")

if num1 == 5:
    print("Five")

# if ... else statement
num1 = 10
if num1 >=10:
    print("num1 >=10")
else:
    print("num1 < 10")

# if ... elif statements
num1 = 5
if num1==0:
    print("Zero")
elif num1==1:
    print("One")
elif num1==2:
    print("Two")
elif num1==3:
    print("Three")
elif num1==4:
    print("Four")
elif num1==5:
    print("Five")
else:
    print("Other")

# nested if statement
num1 = 10
num2 = 20
num3 = 30

if num1>=num2:
    if num1>=num3:
        print(num1)
if num2>=num1:
    if num2>=num3:
        print(num2)
if num3>=num1:
    if num3>=num2:
        print(num3)