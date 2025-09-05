def apply(func, value):
    return func(value)


def square(x: int):
    return x * x


print(apply(square, 5))


def make_adder(n: int):
    def adder(x: int):
        return x + n
    return adder


add5 = make_adder(5)
print(add5(10))
