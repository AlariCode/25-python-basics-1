user = {"age": 37, "name": 1}
user["city"] = "Moscow"

for key in user:
    print(key)

for key in user.keys():
    print(key)

for key, value in user.items():
    print(f"{key}: {value}")

for value in user.values():
    print(value)
