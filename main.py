a = {1, 2}
b = {1, 2, 3}
c = {3, 1, 2}

print(a.issubset(b))
print(b.issubset(a))

print(a.issuperset(b))
print(b.issuperset(a))

print(c == b)
print(c != b)

a.clear()
print(a)

d = b.copy()
print(d == b)
