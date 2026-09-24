product_1 = {
    "name" : "键盘",
    "quantity" : 10
}
product_2 = {
    "name" : "鼠标",
    "quantity" : 20
}
product_3 = {
    "name" : "毛巾",
    "quantity" : 30
}
product_4 = {
    "name" : "数据线",
    "quantity" : 40
}
product_5 = {
    "name" : "牙刷",
    "quantity" : 50
}
products = [product_1,product_2,product_3,product_4,product_5]
orders_products = sorted(
    products,
    key = lambda product : product["quantity"],
    reverse = True
)
print(orders_products[:3])