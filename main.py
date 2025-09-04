s = {1, 2, 3}

s.add(4)
print(s)

s.update([5, 6])
print(s)

s.remove(2)
print(s)

s.discard(3)
s.discard(7)
print(s)

removed_item = s.pop()
print(removed_item)
print(s)

print(4 in s)
print(7 in s)

for el in s:
    print(el)
