num = [10, 15, 20, 25, 30]
# evens = []

# for n in num:
#     if n % 2 == 0:
#         evens.append(n)

# print(evens)


# def is_even(x: int) -> bool:
#     if x % 2 == 0:
#         return True
#     return False


# evens = list(filter(is_even, num))
# print(evens)
evens = list(filter(lambda x: x % 2 == 0, num))
print(evens)

even_comp = [x for x in num if x % 2 == 0]
print(even_comp)
