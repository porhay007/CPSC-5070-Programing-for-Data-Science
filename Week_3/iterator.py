'''

for i in range(10):
    print(i, end= ' ')
    
#Iterating over lists

for value in [2,4,6,8,10]:
    print(value + 1, end= ' ')
    
iter([2,4,6,8,10])


I = iter([2,4,6,8,10])
print(next(I))

print(next(I))

print(next(I))

iter(range(10))


for i in range(10):
    print(i, end= ' ')

    
N = 10 ** 12


for i in range(N):
    if i >= 10:
        break
    print(i, end= ' ')

    
from itertools import count


for i in count():
    if i >= 10:
        break
    print(i, end= ' ')
    

    
l = [2,4,6,8,10]
for i in range(len(l)):
    print(i, l[i])
    
for i, val in enumerate(l):
    print(i, val)
    

#Map function : The map iterator takes a function and applies it to the values in an iterator:
square = lambda x: x ** 2
for val in map(square, range(10)):
    print(val, end = ' ')



# Filter function : 
is_even = lambda x : x % 2 == 0
for val in filter(is_even, range(10)):
    print(val, end = ' ')
    


print(* range(10))

print(*map(lambda x : x ** 2, range(10)))

print(* filter(lambda x : x %2 ==0, range(100)))


#zip function
L1 = (1,2,3)
L2 = ('A', 'B', 'C')

z = zip(L1, L2)
print(*z)

#Unzip
z = zip(L1,L2)
new_L1, new_l2 = zip(*z)
print(new_L1)
print(new_l2)

# Specialized iterators
from itertools import permutations
p =  permutations(range(3))
print(*p)


from itertools import combinations
c = combinations(range(4),3)
print(*c)
from itertools import product
p = product('ab', range(5))
print(*p)


for v in {2,4,6,8}:
    print(v , end= ' ')
    


myiter = iter([2,4,6,8])
print(myiter)

print(type(myiter))

print(next(myiter))

print(next(myiter))


myiter2 = iter([2,4,6])
print(next(myiter2))

## Enumerate

L = list('abcd')

for i, v in enumerate(L):
    print(i,v)
    


L = [1,2,3,4,5,6]
R = list('abcdef')

print(list(zip(L,R)))


D = 'porhaylove'
E = [1,4,6,8,9]

print(list(zip(D,E)))


# map and filter

def square(x):
    return x*x

print(list(map(square, range(10))))

#Exercise



my_str = ['one', 'two', 'three', 'four']

print(list(map(len, my_str)))


# print out even number from range(10)

print(list(filter(lambda x: x%2 == 0,range(10))))

def even (x):
    return x %2 == 0

print(list(filter(even , range(10))))

# exercise 

my_str = ['one', 'two', 'three', 'four', 'five']


print(list(filter(lambda x:len(x) >3 , my_str)))

# take all even number in range (10), then mutilple them by 5

for i in range(10):
    if i %2 == 0:
        print(i *5, end = '') 


t = filter(lambda x : x%3 == 0, range(50))

print(list(map(lambda x : x*5, t)))


print(list(map(lambda x : x*5, filter(lambda x : x%2 == 0, range(10)))))
'''


print([num ** 0.5 for num in range(10)])



L = []
for i in range(2):
    for j in range(3):
        L.append((i,j))
        
print(L)


print([(i,j) for i in range(2) for j in range(4) ])


my_str = ['one', 'two', 'three', 'four', 'five']

print([i for i in my_str if len(i) > 3])