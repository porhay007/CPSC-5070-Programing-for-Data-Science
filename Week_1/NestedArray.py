x = ['a',['e','f'],'c']
#y = x

y = x.copy()

x[1].append('g')


print(x)
print(y)
print(x is y)
print(x == y)