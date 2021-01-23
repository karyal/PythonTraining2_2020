from array import *

# Exploring Array Class
print(dir(array))
print(help(array))

my_array = array("i",[1,2,3,4,5])
print(type(my_array))
print(id(my_array))
print(len(my_array))
print(my_array)

# indexing
print(my_array[0])
print(my_array[4])
print(my_array[-5])
print(my_array[-1])
#print(my_array[5])# IndexError: array index out of range
#print(my_array[-6]) # IndexError: array index out of range

# Slicing
print(my_array[:])
print(my_array[::1])
print(my_array[0:])
print(my_array[0:5])

# Methods
my_array=array("i",[])

#append(self, v, /)
my_array.append(2)
my_array.append(3)
my_array.append(4)
my_array.append(5)
my_array.append(5)
print(my_array)

#count(self, v, /)
print(my_array.count(2))

# extend(self, bb, /)
my_array.extend([1,2,3])
print(my_array)

#index(self, v, /)
print(my_array.index(2))

#insert(self, i, v, /)
my_array.insert(0, 20)
print(my_array)

#pop(self, i=-1, /)
my_array.pop()
print(my_array)

#remove(self, v, /)
my_array.remove(2)
print(my_array)

#reverse(self, /)
print(my_array)
my_array.reverse()
print(my_array)

#tostring(self, /)
print(my_array.tostring())

# More than 1 dimension
my_list = [[1,2,3],[4,5,6],[7,8,9]]
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])

print(my_list[0][0])
print(my_list[0][1])
print(my_list[0][2])

print(my_list[1][0])
print(my_list[1][1])
print(my_list[1][2])

print(my_list[2][0])
print(my_list[2][1])
print(my_list[2][2])