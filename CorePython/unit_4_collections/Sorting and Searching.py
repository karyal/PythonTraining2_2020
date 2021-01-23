# Sorting
# 1. Bubble Sort
def bubble_sort(items):
    swap_again=True
    n=len(items)
    while n>0 and swap_again==True:
        n=n-1
        swap_again=False
        for i in range(n):
            if items[i]>items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
                swap_again=True
    return items

# 2. Insertion Sort
def insertion_sort(items):
    n=len(items)
    for i in range(1, n):
        value = items[i]
        j = i
        while j>0 and items[j-1]>value:
            items[j] = items[j-1]
            j=j-1
        items[j]=value
    return items

items = [5,7,10,1,2,4,9,7,3,6,8]
print(items)
print(bubble_sort(items))
items = [5,7,10,1,2,4,9,7,3,6,8]
print(items)
print(insertion_sort(items))

# Searching
# 1. Linear Search
def linear_search(items, search_term):
    i=0
    result=False
    while i<len(items) and result == False:
        if items[i] == search_term:
            result=True
        else:
            i+=1
    return result

# 2. Binary Search
def binary_search(items, search_term):
    result = False
    first = 0
    last = len(items)-1
    while first<=last and result==False:
        midpoint = (first +last)//2
        if items[midpoint] == search_term:
            result = True
        else:
            if items[midpoint]<search_term:
                first=midpoint+1
            else:
                last = midpoint - 1
    return result

items = [5,7,10,1,2,4,9,7,3,6,8]
print(linear_search(items, 8))
print(linear_search(items, 50))

print(binary_search(items, 8))
print(binary_search(items, 50))

