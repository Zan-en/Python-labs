producty = [
    {"name": "Мяч Wilson", "price": 120, "prodali": 10},
    {"name": "Мяч Molten", "price": 150, "prodali": 7},
    {"name": "Кроссовки Jordan", "price": 290, "prodali": 20},
    {"name": "Кроссовки Puma Lamelo", "price": 265, "prodali": 25}

]



print(f"По каждому товару: ")
for product in producty:
    summ = product["prodali"] * product["price"]
    print(f"{product["name"]} - {summ}")

max_summ = 0
luchsh_product = ""

for product in producty:
    summ = product["prodali"] * product["price"]
    if summ > max_summ:
        max_summ = summ
        luchsh_product = product["name"]


print(f"Самым прибыльным товаром можно считать - {luchsh_product}, Общая сумма товара: {max_summ}")
