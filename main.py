# Нужно нормализовать данные, убрав пробелы + большая первая буква
# и привидя age к числу
users = [
    {"name": "  anton ", "age": "25"},
    {"name": "KATE", "age": " 30 "},
    {"name": "Oleg", "age": "22"}
]


def normalize(user: dict[str, str]) -> dict:
    return {
        "name": user["name"].strip().capitalize(),
        "age": int(user["age"].strip())
    }


normalized_users = list(map(normalize, users))
print(normalized_users)
