password = "hello, PurpleSchool!O "
print(password.count("o"))
print(password.endswith("h"))
print(password.startswith("h"))
print(password.find("o"))
print(password.find("o", 10))
print(password.find("[]"))
print(password.index("o"))
print(password.rfind("o"))
print(password.isnumeric())
print("123".isnumeric())

t = password.split("o")
print(t)

role = ["Admin", "User"]
all_roles = " ".join(role)
print(all_roles)
