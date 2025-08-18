a = [[0, 1], 2, 3, 4, 5]
print(a[0:3])
print(a[:3])
print(a[2:])
b = a[:]
a[0][0] = 10
print(a)
print(b)

c = [0, 1, 2, 3, 4, 5, 6]
print(c[0:5:2])
print(c[0::2])
print(c[::3])
print(c[-4:-1:2])
print(c[-1:-4:-1])
