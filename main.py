a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a.union(b))

print(a & b)
print(a.intersection(b))

a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a - b)
print(b - a)

print(a ^ b)
print(a.symmetric_difference(b))
