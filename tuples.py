# tuples
# immutable but member objects may be mutable

x=()
x=(1,2,3)
# parenthesis optional
x=1,2,3
# single item tuple
x=2,
list1=[]
x=tuple(list1)

# del(x[1]) error
# x[1]=8 error

# 2 item tuple:list and int member objects mutable
x=([1,2],3)
del(x[0][1])
print(x)