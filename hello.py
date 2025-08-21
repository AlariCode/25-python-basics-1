# Проверка email
# a@a.ru - True
# d@.ru - False
# a@a.r - False
# d@com - False
# d@@com - False
# dcom - False
# @s.com - False
# a@.com - False
email = input("Введите email для проверки: ")

if email.count("@") != 1:
    print("Нет")
    exit()

local, domain = email.split("@")

if not local:
    print("Нет")
    exit()
if "." not in domain:
    print("Нет")
    exit()
if len(domain.split(".")[-1]) < 2:
    print("Нет")
    exit()
if len(domain.split(".")[0]) == 0:
    print("Нет")
    exit()
print("Да")
