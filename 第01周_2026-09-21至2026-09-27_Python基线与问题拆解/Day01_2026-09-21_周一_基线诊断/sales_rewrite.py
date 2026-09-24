product_1 = {
    "name": "手机",
    "type": "数码产品",
    "price": 5000,
    "quantity": 12
}
product_2 = {
    "name": "水杯",
    "type": "生活用品",
    "price": 20,
    "quantity": 40
}
product_3 = {
    "name": "手办",
    "type": "娱乐用品",
    "price": 200,
    "quantity": 10
}
products = [product_1,product_2,product_3]
total_sales = 0
max_product = ''
max_sales = 0
for product in products:
    current_sales = product["price"] * product["quantity"]
    total_sales += current_sales
    if current_sales > max_sales:
        max_sales = current_sales
        max_product = product["name"]
print(f'商品的总销售额为{total_sales}')
print(f'销售额最高的商品名称为{max_product},其销售额为{max_sales}')