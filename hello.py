t = (1, 2, 3)
t1 = 1, 2, 3
print(t[0])
print(t[-1])

t = (1, "1", [1, 2])
t[-1][0] = 8
print(len(t))

l = list(t)
print(l)
