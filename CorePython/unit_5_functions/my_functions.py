# Categories of function
def f1():
    print("Hello world of python functions")

def print_message(str_message):
    print("Message : ", str_message)

def do_add():
    n1 = 20
    n2 = 30
    n3 = n1+n2
    print("SUM : ", n3)

def do_add_2():
    n1 = int(input("Enter first no : "))
    n2 = int(input("Enter first no : "))
    n3 = n1+n2
    print("SUM : ", n3)

def do_add_3(n1, n2):
    n3 = n1+n2
    return n3

# Function Arguments

# Fixed Argument
def doAdd(n1, n2):
    print("Sum : ", (n1+n2))

def doAdd2(n1, n2, n3=0):
    print("Sum : ", (n1+n2+n3))

def doAdd3(n1=0, n2=0):
    print("Sum : ", (n1+n2))

def doAdd4(*args):
    for object in args:
        sum = 0
        for item in object:
            sum = sum+int(item)
        else:
            print("Sum : ", sum)

# Recrusive Function
def doAdd5(num1):
    if num1==1:
        return 1
    else:
        return num1+doAdd5(num1-1)

def doFact(num1):
    if num1==0:
        return 1
    else:
        return num1*doFact(num1-1)

def print_string(str):
    if len(str)>0:
        print(str[0], end="")
        print_string(str[1:])

def print_reverse_string(str):
    if len(str)==0:
        return
    tmp = str[0]
    print_reverse_string(str[1:])
    print(tmp, end="")

# Nested Function
def outer(num1):
    def inner(num2):
        return num2+1
    tmp_num =inner(num1)
    print(tmp_num)

# Lambda Function
increase = lambda n:n+1
decrase = lambda n:n-1
sum = lambda n1, n2: n1+n2
dif = lambda n1, n2: n1-n2
prd = lambda n1, n2: n1*n2
div = lambda n1, n2: n1//n2

my_list = [2,3,4,5,6]
new_list = list(filter(lambda x : x%2==1, my_list))

my_list = [2,3,4,5,6]
new_list1 = list(filter(lambda x : x%2==0, my_list))

