def apply(func, value):
    return func(value)


print(apply(lambda x: x + 100, 5))
print(apply(lambda s: s.upper(), "hi"))
