def divide(a: float, b: float):
    if b == 0:
        raise ZeroDivisionError({"error": 1})
    return a / b


def calculate():
    try:
        divide(10, 0)
    except ZeroDivisionError as e:
        print("Деление на 0")
        print(e)
        raise


try:
    calculate()
except ZeroDivisionError:
    print("Поймали выше")
