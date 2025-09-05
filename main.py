# 1.	Проверьте, что у пользователя есть все обязательные документы
# 2.	Равны ли наборы документов?
# 3.	Выведите список лишних документов, которые пользователь добавил.

required_docs = frozenset({"паспорт", "ИНН", "СНИЛС"})
user_docs = {"паспорт", "ИНН", "СНИЛС", "диплом"}

print(f"Обязательные: {required_docs.issubset(user_docs)}")
print(f"Равны ли: {required_docs == frozenset(user_docs)}")
print(f"Лишние: {user_docs - required_docs}")
