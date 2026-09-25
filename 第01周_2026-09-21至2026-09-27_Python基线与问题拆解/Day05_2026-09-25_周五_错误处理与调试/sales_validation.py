def calculate_product_revenue(product):
    if "price"  not in product or "quantity" not in product:
        return None
    price = product["price"]
    quantity = product["quantity"]
    
    try:
        price = float(price)
    except (ValueError,TypeError):
        return None

    if  not isinstance(quantity,int):
        return None
    
    if price < 0 or quantity < 0:
        return None
    else:
        return price * quantity

product_1 = {"name": "毛巾", "price": 19.9, "quantity": 3}
product_1_1 = {"name": "毛巾", "price": "十九元九角", "quantity": 3}
product_1_2 = {"name": "毛巾", "price": 19.9, "quantity": "3"}
product_2 = {"name": "牙刷", "price": 8, "quantity": 0}
product_3 = {"name": "笔", "price": 2}
product_4 = {"name": "本子", "price": -5, "quantity": 2}
product_5 = {"name": "本子"}

print(calculate_product_revenue(product_1))
print(calculate_product_revenue(product_1_1))
print(calculate_product_revenue(product_1_2))
print(calculate_product_revenue(product_2))
print(calculate_product_revenue(product_3))
print(calculate_product_revenue(product_4))
print(calculate_product_revenue(product_5))
print(calculate_product_revenue({"price": None, "quantity": 3}))
print(calculate_product_revenue({"price": 10, "quantity": -1}))