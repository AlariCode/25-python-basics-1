# Написать функцию calculate, которая принимает 2 числа и операцию
# "+" "-" "*" "/"
from typing import Literal


def calculate(a: float, b: float, operation: Literal["+", "-", "*", "/"]):
    """
    Делает математическую операцию над 2-мя числами

    :param a: Первое число
    :param b: Первое число
    :return: Число или строка ошибки
    """
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b if b != 0 else "Ошибка: деление на 0"
        case _:
            return "Неизвестная операция"


print(calculate(10, 5, "+"))
# print(calculate(10, 0, "1"))
