def avg(*args: int):
    return sum(args)/len(args)


print(avg(1, 2, 3))
print(avg(34, 100, 10, 10, 60, 90))


def print_data(name: str, *data: str):
    print(name, data)


print_data("Vasia", "a", "b", "c")
