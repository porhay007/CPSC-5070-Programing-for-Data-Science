'''
print([i for i in range(10) if i % 3 == 0])

## Basic list comprehension

L = [] 
for i in range(12):
    L.append(i **2)
    
print(L)

## multiple iteration
print([(i,j) for i in range(2) for j in range(3)])


## Conditonal on the iterator

print([val for val in range(20) if val % 3 >0])


L = []

for val in range(20):
    if val % 3 > 0:
        L.append(val)
print(L)

# Condtional on the values

val = -10
print(val if val >= 0 else - val)


print([val if val %2 else -val 
 for val in range(20) if val % 3])

print({n**2 for n in range(12)})

print({a % 3 for a in range(1000)})

print({n:n**2 for n in range(6)})

print((n**2 for n in range(12)))
'''

