user = {"age": 37, "name": 1}
print(user["name"])
user["age"] = 20
print(user)

# print(user["city"])
print(user.get("city", "Moscow"))
value = user.pop("age")
print(value)
print(user)

exist = "name" in user
print(exist)
