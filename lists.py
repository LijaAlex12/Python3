# creating new list
# x=list()
# x=['a',25,'dog','8.43']
# x=list(tuple1)


x=[m for m in range(8)]
print(x)

x=[z**2 for z in range(10) if z>4]
print(x)

# delete item or complete list
del(x[1])
print(x)
del(x)


# append an item
y=[]
y.append([1,'t'])
print(y)

# extend:to append a sequence to a list
# within same list
# similar to concatenation + of lists
a=[1,2,3]
b=['a','b']
c=['u']
a.extend(b)
a.append(c)
print(a)

# insert :item insertion at given index
p=[5,3,8,6]
q=['d','k']
p.insert(1,7)
p.insert(3,q)
print(p)

# pop

