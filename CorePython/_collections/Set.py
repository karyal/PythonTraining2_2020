from array import array

# Exploring set Class
print(dir(set))
print(help(set))

# Declare and Initialize Set
set1 = set()
set1 = {1,2,3,4,5,1,2}

array1 = array("i",[2, 3, 4, 5, 6, 7, 2])
set1 = set(array1)

list1 = [2, 3, 4, 5, 6, 7, 1, 2]
set1 = set(list1)

tup1 = (7, 8, 9, 6, 5, 8, 7)
set1 = set(tup1)

print(type(set1))
print(id(set1))
print(len(set1))
print(set1)

# Methods
set1 = {7, 8, 9, 6, 5, 8, 7}
set1.add(2)
print(set1)

set1.update([1,2,3,4,5])
print(set1)

set1.discard(1)
print(set1)

set1.remove(4)
print(set1)

set1.clear()
print(set1)

# Set Operations
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print(set1 - set2)
print(set1 | set2)
print(set1 & set2)
print(set1 ^ set2)


print(set1.difference(set2))
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))

print(" ")
list1 = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
list2 = [6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15]
set1 = set(list1)
set2 = set(list2)
print(set1)
print(set2)
print(set1 & set2) # Intersection {8, 9, 6, 7}
print(set1 | set2) # Union {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
print(set1 - set2) # Difference {1, 2, 3, 4, 5}
print(set1 ^ set2) # Symmetric Difference {1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15}
