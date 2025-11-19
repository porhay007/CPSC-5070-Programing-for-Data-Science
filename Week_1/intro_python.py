midpoint = 5

lower = []; upper = []

for i in range(10):
    if i < midpoint:
        lower.append(i)
    else:
        upper.append(i)

print("Lower:", lower)
print("Upper:", upper)

lower.append(9)
print()

x = 4.0
print(x.real, "+", x.imag, 'i')

type(x.is_integer())

print(bin(10))
