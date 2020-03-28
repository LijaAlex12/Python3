# lambda a simple 1 line function
# do not use def or return keywords
from functools import reduce
px=lambda x:x*2
# print(px(9))

py=lambda x,y:x+y
print(py(1,2))
mx=lambda x,y:x if x>y else y
print(mx(3,4))

# map:apply same function to each
# element of a sequence
# return the modified list
# list=[m,n,p],function f(n)
# new list [f(m),f(n),f(p)]
n=[4,3,2,1]
newlist=list(map(lambda x:x**2,n))
print(newlist)

ax=lambda x:x**2
list1=[3,4,6]
pq=map(ax,list1)

# here the map fn attatches
# each element of list
# as argument of ax function
pq=list(pq)
print(pq)

# passg normal fns
# print(list(map(square,n)))

# or list comprehension
# print([x**2 for x in list1])

# filter :filter items out of a sequence
# return filtered list
# condition and list passed

n=[4,3,2,1]
print(list(filter(lambda x:x>2,n)))
# or list comprehension
# print([x for x in list1 if x>2])

# reduce
# uses result of operation as first param
# of next operation
# returns an item not list
# use from functools import reduce
m=[4,3,2,1]
print(reduce(lambda x,y:x*y,m))
# 4*3=12
# 12*2=24
# 24*1=24
