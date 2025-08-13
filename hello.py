# Максимум среди 3-х чисел с плавающей точкой
role = input("Введите роль: ")
a = 10
# if role == 'admin':
#     print("Админ")
# elif role == 'manager':
#     print("Менеджер")
# elif role == 'seo':
#     print("SEO специалист")
# else:
#     print("Уборщица")

match role:
    case "admin" | "ADMIN" if a > 0:
        print("Админ") 
    case "manager":
        print("Менеджер") 
    case "seo":
        print("SEO специалист") 
    case _:
        print("Уборщица")

match a:
    case a if a > 0:
        print(">0")
    case _:
        print("<=0")