# print 1- 10
num1 = 1
while num1<=10:
    print(num1)
    num1=num1+1

# print 10 -1
num1 = 10
while num1>=1:
    print(num1)
    num1= num1-1

# sum of 1-10
sum=0
num1=1
while num1<=10:
    sum=sum+num1
    num1 = num1 + 1
else:
    print("Sum:", sum)

# factorial of 1-10
fact=0
num1=1
while num1<=10:
    fact=fact*num1
    num1 = num1 + 1
else:
    print("Fact:", fact)

# odd/even numbers between 1-10
nums= []
num1=1
while num1<=10:
    #if num1%2!=0:
    if num1%2!=1:
        nums.append(num1)
    num1=num1+1
else:
    print("Nums: ", nums)

# nested loop
num1 =1
while num1<=10:
    num2 = 1
    while num2<=10:
        print(num2)
        num2=num2+1
    num1 = num1+1

# dynamic loops
num1 = int(input("enter start no : "))
num2 = int(input("enter stop no : "))
if not num1<=num2:
    num1, num2 = num2, num1
while num1<=num2:
    print(num1)
    num1=num1+1

# break statements
num1 = 0
while num1<=10:
    num1=num1+1
    if num1 == 5:
        continue
    print(num1)
    if num1==8:
        break

# pass statement
class MyClass():
    pass

def function1():
    pass
