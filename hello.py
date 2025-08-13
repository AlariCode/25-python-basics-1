# Максимум среди 3-х чисел с плавающей точкой
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a >= b and a >= c:
    print(a)
elif b >=a and b >= c:
    print(b)
else:
    print(c)