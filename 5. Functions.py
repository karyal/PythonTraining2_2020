# -*- coding: utf-8 -*-
"""
Functions
"""
# Installation and Configuration
# Core Python
# Decisions
# Looping
# Functions

"""
A. Expression - Valid Python Term  # 10 + 30

10  - Expression1
+   - Expression2
30  - Expression3

B. Statement - Collection of Expressions - Perform certain task.

result = 10 + 30

C. Function - Collection of Statements.

Why Function? 
- Write once; Use many
- Grouping source code for specific task - Modulling 

How to create a function

Syntax
def function_name():
    statement_1
    statement_2
    statement_N

function_name : variable_name (identifier)


# Puskar Karki
def sum(a, b):
   return a + b

print( sum( 4, 7) )
print( sum( 9, 2.5 ) 

# Bibek Rawat
def my_function():
    print("Hello from function")

my_function()


# create function in one file (MyFunctions.py)
# call function in another file(test.py)

# Task-1
- Student Info
- rollno, name, standard, sub1, sub2, sub3, sub4
- PM=40
- total, average, result, grade

# Solve by creating different functions.

"""

import MyFunctions # Import Resource File

MyFunctions.print_hello() # Call a function
      