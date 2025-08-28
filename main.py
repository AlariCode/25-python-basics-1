for i in range(100):
    print(i)
    if i >= 10:
        print("Конец цикла")
        break
print("Готово")

for i in range(1, 11):
    if i % 2 == 1:
        continue
    print(i)

for i in range(5):
    print(i)
    if i > 3:
        break
else:
    print("Готово без break")
