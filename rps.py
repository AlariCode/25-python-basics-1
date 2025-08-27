# Пользователь вводи число раудом
# Для каждого раунда вводит камень / ножницы / бумага
# Копьютер выбират случайно и считается результат
# Считается к кого больше побед
# 1. Спрашиваем число раунтов
# 2. Для каждого раунда мы получает выбор и сравниваем
# 3. Показываем итог
import random

CHOICES = ("камень", "ножницы", "бумага")
rount_count = int(input("Сколько раунтов будем играть? "))
user_score = 0
comp_score = 0

for r in range(1, rount_count + 1):
    print(f"\nРаунд {r}:")
    user_select = input("Выбери (камень/ножницы/бумага): ")
    if user_select not in CHOICES:
        print("Некорректный выьбор!")
        exit()
    comp_select = random.choice(CHOICES)
    print(f"Компьютер выбрал: {comp_select}")

    if user_select == comp_select:
        print("Ничья")
    elif (user_select == "камень" and comp_select == "ножницы") or \
            (user_select == "ножницы" and comp_select == "бумага") or \
            (user_select == "бумага" and comp_select == "камень"):
        print("Ты победил!")
        user_score += 1
    else:
        print("Ты проиграл(")
        comp_score += 1

print("====Итог игры====")
print(f"Твой счёт: {user_score}")
print(f"Счёт компьютера: {comp_score}")

if user_score > comp_score:
    print("Ты победил в игре!")
elif user_score < comp_score:
    print("Компьютер победил в игре!")
else:
    print("Ничья")
