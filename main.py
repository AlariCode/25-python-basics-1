# Нужно найти те заказы, для которых сумма > 100 и статус paid
orders = [
    {"id": 1, "user": "Anton", "amount": 150, "status": "paid"},
    {"id": 2, "user": "Kate", "amount": 50, "status": "canceled"},
    {"id": 3, "user": "Oleg", "amount": 200, "status": "paid"},
    {"id": 4, "user": "Ivan", "amount": 0, "status": "draft"},
    {"id": 5, "user": "Maria", "amount": 120, "status": "paid"}
]

filtered_orders = list(filter(
    lambda o: o["status"] == "paid" and o["amount"] > 100,
    orders
))

print(filtered_orders)
