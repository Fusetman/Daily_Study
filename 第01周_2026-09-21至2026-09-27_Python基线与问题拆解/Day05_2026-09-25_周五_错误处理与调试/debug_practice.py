price = "19.9"
quantity = 3

revenue = float(price) * quantity

print(revenue)
print(type(revenue))

total = revenue + 10

print(total)


product = {"name": "毛巾", "price": 19.9,"quantity": 3}
if "quantity" in product:

    quantity = product["quantity"]
    revenue = product["price"] * quantity
    print(revenue)
else:
    print('缺少销量无法计算')


price_text = "19.9"
try:    
    price = float(price_text)
    print(price)
except ValueError:
    print("价格格式错误，无法计算")


sales = [100, 200, 300]
for amount in sales:
    print(amount)


product = {"name": "毛巾", "price": -19.9, "quantity": 3}
if product["price"] < 0:
    print('价格不能为负数')
else:
    print(product['price'] * product['quantity'])


products = [100,200,300]
total_sales = 600
if products:
    average = total_sales / len(products)
    print(average)
else:
    print("没有商品数据，无法计算平均值")
