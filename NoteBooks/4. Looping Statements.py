# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

# Print Hello 10 time.

# Looping Statements
"""
Repeat specific tasks multiple times.
    
# How to design loop
    start_value = 1
    stop_value = 10
    condition = start_value <= stop_value
    statement = print("Hello")
    modifier = start_value increased by 1

# 1. While Loop
#Example-1
start_value = 1
stop_value = 10
while(start_value<=stop_value):
    print("Hello")
    start_value+=1

# Example-2
start_value = 1
stop_value = int(input("How many time ? "))
while(start_value<=stop_value):
    print("Hello")
    start_value+=1


# Print 1 ten times.     
start_value = 1
stop_value = 10
value = 1
while(start_value<=stop_value):
    print(value)
    start_value+=1

# Print 1 N times.     
start_value = 1
stop_value = int(input("How many times ? : "))
value = 1
while(start_value<=stop_value):
    print(value)
    start_value+=1


# Print 1-10.
start_value = 1
stop_value = 10
while (start_value<=stop_value):
    print(start_value)
    start_value+=1

# Print 10-1.
start_value = 10
stop_value = 1
while (start_value>=stop_value):
    print(start_value)
    start_value-=1


# Print even numbers between 1 to 10.
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 - [2, 4, 6, 8, 10]
# 10/2 if remainder equals to 0 than number if even.

start_value = 1
stop_value = 10
while (start_value<=stop_value):
    if start_value % 2 == 0:
        print(start_value)
    start_value+=1


# Print odd numbers between 1 to 10.
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 - [1, 3, 5, 7, 9]
# 10/2 if remainder equals to 1 than number if odd.

start_value = 1
stop_value = 10
while (start_value<=stop_value):
    if start_value % 2 == 1:
        print(start_value)
    start_value+=1


# Print sum of 1 to 10.
start_value = 1
stop_value = 10
sum = 0
while (start_value<=stop_value):
    sum+=start_value
    start_value+=1
print(sum)


# 2. for loop

# Print Hello 10 times.
for i in range(10):# i = 0 to Less than 10 (0-9)
    print("Hello")


# Print 1 10 times.
num1 = 1
for i in range(10):
    print(num1)

# Print 1 to 10.
for i in range(10):
    print(i)
# 0-9

for i in range(1, 11):
    print(i)


# Print 1 to 10 - odd/even numbers.
for i in range(1, 11):
    if i%2==0:
        print(i)
print()
for i in range(1, 11):
    if i%2==1:
        print(i)

sum=0
for i in range(1, 11):
    sum+=i
print(sum)

# Nested Loop
for i in range(1, 6):
    for j in range(6, 11):
        print(i, j)

# Loop with list/tuple/set

list1 = [7, 3, 4, 5, 6, 7, 8, 7,3,2,2,3,4,5]

# Style-1
for i in range(len(list1)):
    print(list1[i])

print()
# Style-2
for item in list1:
    print(item)
print()    

# Looping with dictionary
dict1 = {'sn':1, 'name':'Krishna', 'address':'KTM'}

for key, value in dict1.items():
    print(key, value)

print()        
for key in dict1.keys():
    print(dict1[key])

print()    
for value in dict1.values():
    print(value)

# Break Statement
for i in range(1, 11):
    if i == 5:
        break
    print(i)

print()
# Continue Statement
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# return
def how_r_y():
    return "I am fine"

print(how_r_y())


# pass
def what_is_your_name():
    pass

print(what_is_your_name())


# Steps in Loop
for i in range(1, 11):
    print(i)
"""

