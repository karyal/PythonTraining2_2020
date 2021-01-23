#Basic Types
# Boolean
var1 = True
print(type(var1))
print(id(var1))
#print(len(var1))
print(var1)

var1 = False
print(type(var1))

# Numeric
# integer
var1 = 10
print(type(var1))# int
print(id(var1))
#print(len(var1))
print(var1)

# float
var1 = 10.258
print(type(var1))# float
print(id(var1))
#print(len(var1))
print(var1)

# complex
var1 = 10+5J
print(type(var1))# complex
print(id(var1))
#print(len(var1))
print(var1)

# String
var1 = "Kathmandu, Nepal"
print(type(var1))# complex
print(id(var1))
print(len(var1))
print(var1)

# Array
from array import array
var1 = array("i",[1, 4, 5, 2, 3])
print(type(var1))# array
print(id(var1))
print(len(var1))
print(var1)

# List
var1 = [1, 4, 5, 2, 3]
print(type(var1))# list
print(id(var1))
print(len(var1))
print(var1)

for item in var1:
    print(item)

# Tuple
var1 = (1, 4, 5, 2, 3)
print(type(var1))# tuple
print(id(var1))
print(len(var1))
print(var1)

# Set
var1 = {1, 4, 5, 2, 3}
print(type(var1))# set
print(id(var1))
print(len(var1))
print(var1)

#Dictionary
var1 = {'id':1, 'name':'Krishna'}
print(type(var1))# dict
print(id(var1))
print(len(var1))
print(var1)

for key in var1:
    print(var1[key])

# Type Conversion

# Boolean
# string to bool
str1 = "True"
var1 = bool(str1)
print(type(var1))

# bool to string
var1 = False
str1 = str(var1)
print(type(str1))

# int to bool
val1 = 1
var1 = bool(val1)
print(type(var1))

# bool to int
val1 = False
var1 = int(val1)
print(type(var1))

# Integer
# String to Integer
value1 = "1"
var1 = int(value1)
print(type(var1))

# Integer to String
value1 = 1
var1 = str(value1)
print(type(var1))

#Note: String to Float/Float to String

# Array to List
values = array('i',[1,2,3,4,5])
var1 = list(values)
print(type(var1))

# Array to Tuple
values = array('i',[1,2,3,4,5])
var1 = tuple(values)
print(type(var1))

# Array to Set
values = array('i',[1,2,3,4,5])
var1 = set(values)
print(type(var1))

# List to Array
values = [1,2,3,4,5]
var1 = array('i', values)
print(type(var1))

# List to Tuple
values = [1,2,3,4,5]
var1 = tuple(values)
print(type(var1))

# Tuple to Array
values = (1,2,3,4,5)
var1 = array('i', values)
print(type(var1))

# Tuple to List
values = (1,2,3,4,5)
var1 = list(values)
print(type(var1))

# Tuple to Set
values = (1,2,3,4,5)
var1 = set(values)
print(type(var1))

# None
var1 = None
print(var1)