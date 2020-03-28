# creating new dictionary
x={'pork':25,'beef':33,'chicken':22}

x=dict( [ ('pork',8),('beef',9),('chicken',8) ] )

x=dict(a=2,b=3,c=3)
print(x)
# dict oprn

# add or change item in x
x['beef']=9
print(x)
x['b']=6
print(x)

# remove item from dict
del x['beef']
print(x)
# check membership looks for keys not values
print('a' in x)
print('a' not in x)

# length
print(len(x))
# delete all items from dict
x.clear()
print(x)
# delete dict x
del x
# print(x)

# accessing keys and values in dict
x={'pork':25,'beef':33,'chicken':22}
print(x.keys())
print(x.values())
# list of key value tuple pairs
print(x.items())
# tests membership in x
print(33 in x.values())
print('beef' in x.keys())

# iterating a dict entries in dict are in random order
for key in x:
    print(key,x[key])
for key,value in x.items():
    print(key,value)
