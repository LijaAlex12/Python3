# creating a new set

x={2,3,3,4}
print(x)
x=set()
# strips duplicates
list1=[]
x=set(list1)

# set comprehension random order
x={x for x in range(10) if x>5}
print(x)

# set operations
x=set()
# add item
x.add(4)
print(x)
# remove item
x.remove(4)
print(x)
# get length
print(len(x))
# membership in x
print(4 in x)
print(4 not in x)
# pop random item from set
x={31,2,3,4,5,6}
x.pop()
print(x)
# delete all items from set x
x.clear()
print(x)

# standard mathematical operations
set1=()
set2=()
set1&set2
set1|set2
# symm diff
set1^set2
set1-set2
# set2 contains set1
set1<=set2
# set1 contains set2
set1>=set2
