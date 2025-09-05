num = [1, 2, 3, 4, 5]
# res = []

# for n in num:
#     res.append(n * n)

# print(res)


# def square(x: float):
#     return x * x

# squares_itarator = map(lambda x: x * x, num)

squares = list(map(lambda x: x * x, num))
print(squares)

# for el in squares_itarator:
#     print(el)

a = [1, 2, 3]
b = [10, 20, 30]

sums = list(map(lambda x, y: x + y, a, b))
print(sums)
