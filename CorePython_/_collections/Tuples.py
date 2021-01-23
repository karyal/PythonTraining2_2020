from array import array
# Tuple
print(dir(tuple))
print(help(tuple))

# Declare & Initialize
tup1 = ()
tup1 = tuple()
tup1 = (1, 2, 3, 4, 5)
tup1 = (1, 2.456, 3+4J, True, "Kathmandu")
tup1 = (1, 2.456, 3+4J, True, "Kathmandu",array('i',[3,4,5,6]))
tup1 = (1, 2.456, 3+4J, True, "Kathmandu",array('i',[3,4,5,6]), [10,11,12,13])
tup1 = (1, 2.456, 3+4J, True, "Kathmandu",array('i',[3,4,5,6]), [10,11,12,13], (5,6,7,8,9))
tup1 = 1,2,3,4,5
tup1 = "Kathmandu","Bhaktapur","Lalitpur"

# Array to Tuple
array1 = array("i",[1,2,3,4,5])
tup1 = tuple(array1)
# List to to Tuple
list1 = [1,2,3,4,5]
tup1 = tuple(list1)

print(type(tup1))
print(id(tup1))
print(len(tup1))
print(tup1)

# Methods
#1. count(self, value, /)
tup1 = (1, 2.456, 3+4J, False, "Kathmandu")
print(tup1.count(1))

#2. index(self, value, start=0, stop=2147483647, /)
from random import seed
from random import randint

values = []
for _ in range(1, 20):
    values.append(randint(1, 20))
tup1 = tuple(values)
print(tup1)
value = 10
count = tup1.count(value)
if count>=1:
    print(tup1.index(value, 0, len(tup1)))# ValueError: tuple.index(x): x not in tuple
else:
    print("Not found!")