# Пользователь вводи число раудом
# Для каждого раунда вводит камень / ножницы / бумага
# Копьютер выбират случайно и считается результат
# Считается к кого больше побед
# 1. Спрашиваем число раунтов
# 2. Для каждого раунда мы получает выбор и сравниваем
# 3. Показываем итог
import random


def select_variant():
    user_select = None
    while user_select not in CHOICES:
        user_select = input("Выбери (камень/ножницы/бумага): ")
        if user_select not in CHOICES:
            print("Некорректный выбор!")
    return user_select


def compute_game_result(user_ch: str, comp_ch: str):
    if user_ch == comp_ch:
        print("Ничья")
        return (0, 0)
    elif (user_ch == "камень" and comp_ch == "ножницы") or \
            (user_ch == "ножницы" and comp_ch == "бумага") or \
            (user_ch == "бумага" and comp_ch == "камень"):
        print("Ты победил!")
        return (1, 0)
    else:
        print("Ты проиграл(")
        return (0, 1)


def print_result(user_res: int, comp_res: int):
    print("====Итог игры====")
    print(f"Твой счёт: {user_res}")
    print(f"Счёт компьютера: {comp_res}")

    if user_res > comp_res:
        print("Ты победил в игре!")
    elif user_res < comp_res:
        print("Компьютер победил в игре!")
    else:
        print("Ничья")


CHOICES = ("камень", "ножницы", "бумага")
rount_count = int(input("Сколько раунтов будем играть? "))
user_score = 0
comp_score = 0

for r in range(1, rount_count + 1):
    print(f"\nРаунд {r}:")
    user_select = select_variant()
    comp_select = random.choice(CHOICES)
    print(f"Компьютер выбрал: {comp_select}")
    [user_mod, comp_mod] = compute_game_result(user_select, comp_select)
    user_score += user_mod
    comp_score += comp_mod
print_result(user_score, comp_score)
