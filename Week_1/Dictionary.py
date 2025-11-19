import copy

numbers = {'one':1, 'two':2, 'three':3}

print(numbers['two'])


numbers['ninety'] = 90
print(numbers)

primes = {2, 3, 5, 7}
odds = {1, 3, 5, 7, 9}

primes | odds      # with an operator
print(primes.union(odds))

primes & odds             # with an operator
print(primes.intersection(odds))

primes - odds           # with an operator
print(primes.difference(odds))

primes ^ odds                     # with an operator
print(primes.symmetric_difference(odds))

print(list(range(1, 10, 2)))


for n in range(20):
    if n % 2 == 0:
        continue
    print(n, end = ' ')


print(complex(1, 2))

print(type(odds))
print(float(1))

print("0.2 = {0:.8f}".format(0.7))

print(complex(2))

c = 3+ 4j
print(c.real)
print(c.imag)
print(c.conjugate())
print(abs(c))



return_value = print("Hello")

print(1,2,4,5,6, sep=" a ")

def fibonacci(N):
    L = []
    a, b = 0, 1
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L

print(fibonacci(10))


def real_imag_conj(val):
    return val.real, val.imag, val.conjugate()

r, i, c = real_imag_conj(3 + 4j)
print(r, i, c)


a = [1, ["a", "b", "c"], 3]
b = a

print(a == b)
print(a is b)

print( 0==0 & False)


x = [1,2,[3,4],5]

y = copy.copy(x)

x.append(6)

x[2].append(7)
print(x)
print(y)