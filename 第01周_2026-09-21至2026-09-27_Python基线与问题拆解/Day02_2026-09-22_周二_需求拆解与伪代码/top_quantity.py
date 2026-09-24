product_1 = {
    "name" : "小米13",
    "price" : 2099,
    "quantity" : 25
}
product_2 = {
    "name" : "天选5pro",
    "price" : 7999,
    "quantity" : 24
}
product_3 = {
    "name" : "华为freeclip 2",
    "price" : 1099,
    "quantity" : 28
}
product_4 = {
    "name" : "高驰pace3",
    "price" : 1399,
    "quantity" : 45
}
products = [product_1,product_2,product_3,product_4]
max_name = ""
max_quantity = 0
for product in products:
    if product["quantity"] > max_quantity:
        max_quantity = product["quantity"]
        max_name = product["name"]
print(f'销量最高的商品名称为{max_name},其销量为{max_quantity}')