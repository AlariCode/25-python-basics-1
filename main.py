def print_hello(user_name: str):
    print(f"Привет {user_name}")


print_hello("Антон")
print_hello("Вася")


def multiply(a: int, b: int) -> int:
    return a * b


res = multiply(4, 5)
print(res)
