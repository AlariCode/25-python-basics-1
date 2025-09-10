nums = [5, 2, 9, 1, 7, 10]

print(sorted(nums))
print(sorted(nums, reverse=True))

words = ["banana", "apple", "pear", "ab"]

print(sorted(words))
print(sorted(words, reverse=True))

users = [
    {"name": "Anton", "age": 18},
    {"name": "Maria", "age": 20},
    {"name": "Anna", "age": 20},
    {"name": "Vasia", "age": 50}
]

print(sorted(users, key=lambda u: (-u["age"], u["name"])))
