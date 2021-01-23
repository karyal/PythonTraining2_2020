# print 1- 10
for i in range(1, 10, 1):
    print(i)

# print 10 -1
for i in range(10, 1, -1):
    print(i)

# sum of 1-10
sum=0
for i in range(1, 10, 1):
    print(i)
else:
    print("Sum:", sum)

# factorial of 1-10
fact=0

for i in range(1, 10, 1):
    fact = fact*i
else:
    print("Fact:", fact)

# odd/even numbers between 1-10
nums= []
num1=1
for i in range(1,10,1):
    #if num1%2!=0:
    if num1%2!=1:
        nums.append(num1)
    num1=num1+1
else:
    print("Nums: ", nums)

# nested loop

for i in range(1,10,1):
    for j in range(1, 10, 1):
        print(j)

# dynamic loops
num1 = int(input("enter start no : "))
num2 = int(input("enter stop no : "))

if not num1<=num2:
    num1, num2 = num2, num1

for i in range(num1, num2, 1):
    print(i)

# break statements

for i in range(1, 10, 1):
    if i== 5:
        continue
    print(i)
    if i==8:
        break

# pass statement
class MyClass():
    pass

def function1():
    pass
