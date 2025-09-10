def multiplier(factor: float):
    def inner(x: float):
        return x * factor
    return inner


double = multiplier(2)
triple = multiplier(3)

print(double(10))
print(triple(10))


def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


c1 = make_counter()
c2 = make_counter()
print(c1())
print(c1())
print(c1())
print(c2())
