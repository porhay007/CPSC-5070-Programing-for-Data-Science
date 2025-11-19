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


