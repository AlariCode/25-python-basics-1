# Написать функцию calculate, которая принимает 2 числа и операцию
# "+" "-" "*" "/"

def calculate(a: float, b: float, operation: str):
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
print(calculate(10, 0, "/"))
