# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 18:36:01 2020
@author: Krishna
"""

# Decision Making Statements

"""
1. if statement

Syntax
if condition:
    statement(s) for true (Run)
    
Condition -> bool (True, False)
* ==, !=, >, >=. <, <=

    
# Example-1
num1 = 1
num2 = 5
if (num1>num2):
    print("Hello")
    print("Hi")
    print("How are you?")
print("End")


# Example-2
num1 = int(input("Enter first no : "))
num2 = int(input("Enter second no : "))
if (num1>num2):
    print("Hello")
    print("Hi")
    print("How are you?")
print("End")

2. if ... else statement
Syntax
if Condition:
    Statement for True
else
    Statement for False


Example-1
num1 = 5
if (num1 == 5):
    print("Five")
else:
    print("Others")
    
# Example-2
num1 = input("Enter any number : ")
num1 = int(num1)
if (num1 == 5):
    print("Five")
else:
    print("Others")    

# 3. if ..... elif.... else statement
Syntax
if condition1:
    statement1_for_true
elif condition2:
    statement2_for_true
elif condition3:
    statement2_for_true
else:
    statement4_for_false

# Example
num1 = 10
if num1==0:
    print("Zero")
elif num1==1:
    print("One")
elif num1==2:
    print("Two")
elif num1==3:
    print("Three")
else:
    print("Others")


#4. Nested if Statement
Syntax
if Condition1:
    if Condition2:
        Statment for ture_all

# Example
num1 = 4
num2 = 5
num3 = 6

if num1>num2:
    if num1>num3:
        print(num1)

if num2>num1:
    if num2>num3:
        print(num2)
        
if num3>num1:
    if num3>num2:
        print(num3)


# 5. if statement with multiple conditions

if (Condition1) and (Condition2) and (Condition3):
    Statement_for_true

if (Condition1) or (Condition2) or (Condition3):
    Statement_for_true
    
"""

# Example-1
num1 = 4
num2 = 5
num3 = 6

if (num1>num2) and (num1>num3):
    print(num1)
if (num2>num1) and (num2>num3):
    print(num2)
if (num3>num1) and (num3>num2):
    print(num3)
    
# Example-2
num1 = int(input("Enter first no : "))
num2 = int(input("Enter second no : "))
num3 = int(input("Enter third no : "))

if (num1>num2) and (num1>num3):
    print(num1)
if (num2>num1) and (num2>num3):
    print(num2)
if (num3>num1) and (num3>num2):
    print(num3)    
