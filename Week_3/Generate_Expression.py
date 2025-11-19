'''
print([n **2 for n in range(12)])

print((n ** 2 for n in range(12)))

G = (n ** 2 for n in range(12))

print(list(G))


#A list is a collection of values, while a generator is a recipe for producing values¶

L = [n ** 2 for n in range(12)]
for val in L : 
    print(val, end =  ' ' )
    
from itertools import count



    
factors = [2,3,5,7]
G = (i for i in count() if all(i % n > 0 for n in factors))
for val in G :
    print(val, end = ' ')
    if val > 40 : break
    

L = [n **2 for n in range(12)]
for val in L:
    print(val, end = ' ')


for val in L:
    print(val, end = ' ')
    
G = (n ** 2 for n in range(12))

print(list(G))

print(list(G))


G = (n**2 for n in range(12))
for n in G:
    print(n, end=' ')
    if n > 30: break

print("\ndoing something in between")

for n in G:
    print(n, end=' ')
    
    
L1 = [n ** 2 for n in range(12)]

L2 = []
for n in range(12):
    L2.append(n ** 2)

print(L1)
print(L2)


# yield function

G1 = (n ** 2 for n in range(12))

def gen():
    for n in range(12):
        yield n ** 2

G2 = gen()
print(*G1)
print(*G2)

#Example : Prime Number Generator

L = [n for n in range(2,40)]
print(L)

# Remove all multiples of the first value
L = [n for n in L if n == L[0] or n % L[0] >0]
print(L)

# Remove all multiples of the second value
L = [n for n in L if n == L[1] or n % L[1] > 0]
print(L)


# Remove all multiples of the third value
L = [n for n in L if n == L[2] or n % L[2] > 0]
print(L)


def gen_primes(N):
    """Generate primes up to N"""
    primes = set()
    for n in range(2, N):
        if all(n % p > 0 for p in primes):
            primes.add(n)
            yield n

print(*gen_primes(100))


names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
'''

print([str(a) for a in range(2)])

print([''.join([str(a), str(b), str(c), str(d)]) for a in range(2) for b in range(2) for c in range(2) for d in range(2)]
)