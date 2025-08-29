def exp(num: float, e: float = 2, mul: float = 1) -> float:
    return mul * num ** e


def print_data(name: str, *data: str, sep: str = " "):
    print(name, data, sep)


print(exp(2, 3))
print(exp(e=3, num=2))
print(exp(2, mul=3))
print(exp(2))

print_data("Vasia", "a", sep="1")
