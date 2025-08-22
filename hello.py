name, email, age = "Anton", "a@a.ru", 18
print("Привет " + name + " с почтой " + email + " и " + str(age) + " лет")
print("Привет {} с почтой {} и {} лет".format(name, email, age))
print("Привет {n} с почтой {e} и {a} лет".format(e=email, a=age, n=name))
print(f"Привет {name} с почтой {email} и {age} лет")
print(f"Привет {name} с почтой {email} и {age + 10} лет")
print(f"Привет {name} с почтой {email} и {age:.1f} лет")
