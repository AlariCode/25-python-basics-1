l = [[1, 2], [2, 3]]
c = l.copy()
print(c is l)
l[0][0] = 10
print(c)
print(l)
print(l[0] is c[0])
