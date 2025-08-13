age = input("Введите возраст: ")

if int(age) < 18:
    print("Вам меньше 18")
else:
    if int(age) < 50:
        print("Вам от 18 до 50 лет")
    else:
        print("Вам больше 50 лет")


if int(age) < 18:
    print("Вам меньше 18")
elif int(age) < 50:
    print("Вам от 18 до 50 лет")
else:
    print("Вам больше 50 лет")