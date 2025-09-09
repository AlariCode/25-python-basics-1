from functools import reduce


nums = [1, 2, 3, 4, 5]
print(sum(nums))

res = 0

for n in nums:
    res += n
print(res)


def sum_custom(acc: int, next_el: int):
    return acc + next_el


total = reduce(sum_custom, nums, 10)
print(total)

words = ["Привет!", "Как", "дела?"]
sentence = reduce(lambda a, b: a + " " + b, words)
print(sentence)
