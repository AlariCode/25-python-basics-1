try:
    x = int(input("Введите число: "))
    print(10/0)
# except ValueError:
#     print("Ошибка input!")
# except ZeroDivisionError:
#     print("Ошибка деления на 0!")
except Exception as e:
    print("Ошибка:", e)
finally:
    print("Финал")
print("Продолжение...")
