# Slicing

x =[1, 2, 3, 4, 5, 6, 7]
print(x[::2])

# mutable
 #list

x = ['a', 'b', {'a':{'b':[{'c':'hello'}]}}]

print(x[2]['a']['b'][0]['c'][2:4])

##
set1 = {'a', 'b', "c", 'c'}
set2 = {'b', "c", 'c', 'd'}

set3 = set1.union(set2)
print(set3)

# Use range(start, stop, step) to get odd numbers
#for i in range(1,10,2):
  #  print(i, end = "*")



L = []
max = 100

for n in range(1, max+1):
    for i in range(1, n+1):       # first blank: check all integers from 1 to n
        if i*i == n:              # second blank: if i squared equals n, it's a square number
            break
    else:
        L.append(n)

print(set(L))

squares = set(range(1,101)) - set(L)
print(squares)

x=['a', 'b', 'c', 'd', 'e']
print(x[-2:-5:-1])

x = ('a', 'b', 'c', 'd', 'e')
x = x[:2] + x[3:]
print(x)

x = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Seattle_Center_as_night_falls.jpg'
image_name = x.split('/')[-1]
print(image_name)  # Output: Seattle_Center_as_night_falls.jpg
