from array import array
# Exploring List Class
print(help(list))

# Declare and Initialize
list1 = list(())
list1 = ([1,2,3,4,5])
list1 = ([1,2.5,3+5J,True,"Kathmandu"])
array1 = array("i",[1,2,3,4,5,6])
list1 = list(array1)
list1 = [1,2,3, [3,4,5,6]]
list1 = list(('Apple','Banana'))
list1 = ['Bananas', 'Boysenberries', 'Blueberries', 'Bing Cherry', 'Cherries', 'Cantaloupe', 'Crab apples', 'Clementine', 'Cucumbers']
print(type(list1))
print(id(list1))
print(len(list1))
print(isinstance(list1, list))
print(list1)

# Indexing
print(list1[0])
print(list1[len(list1)-1])
print(list1[-1])
print(list1[-9])
#print(list1[9])# IndexError: list index out of range
#print(list1[-10])# IndexError: list index out of range

# Slicing
print(list1[:])
print(list1[0:])
print(list1[:9])
print(list1[::2])

# in & not in
print('Banana' in list1)
print('Banana' not in list1)

list2 = ['Bananas', 'Boysenberries', 'Blueberries', 'Bing Cherry']
list3 = ['Cherries', 'Cantaloupe', 'Crab apples', 'Clementine', 'Cucumbers']
list4  = list2+list3
print(list4)

# Methods
# append(self, object, /)
list4.append('Damson plum')
print(list4)

# clear(self, /)
list1.clear()
print(list1)

# copy(self, /)
list5 = list4.copy()
print(list1)

# count(self, value, /)
list4.append('Damson plum')
print(list4)
print(list4.count('Damson plum'))

# extend(self, iterable, /)
list4.extend(['Dinosaur Eggs', 'Dates', 'Dewbe'])
print(list4)

# index(self, value, start=0, stop=9223372036854775807, /)
index = list4.index('Dates',0, len(list4))
print(index)

# insert(self, index, object, /)
list4.insert('Elderberry')
print(list4)

# pop(self, index=-1, /)
list4.pop()
print(list4)

list4.pop(3)
print(list4)

# remove(self, value, /)
list4.remove('Elderberry')
print(list4)

# reverse(self, /)
list4.reverse()
print(list4)

# sort(self, /, *, key=None, reverse=False)
list4.sort()
print(list4)

list4.sort(reverse=True)
print(list4)

list4.sort(reverse=False)
print(list4)

# zip()
my_list1 = [1,2,3,4,5]
my_list2 = ['Krishna','Reeta','Rhydam','Rajan','Uttam']
my_list3 = list(zip(my_list1, my_list2))

print(my_list3)
print(type(my_list3))
print(len(my_list3))
print(hex(id(my_list3)))

for item in my_list3:
    print(item)

id, names = zip(*my_list3)
print(id, names)