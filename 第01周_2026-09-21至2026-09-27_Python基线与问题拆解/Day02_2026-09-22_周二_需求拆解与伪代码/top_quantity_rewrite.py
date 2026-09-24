product_1 = {
    "name" : "无线鼠标",
    "type" : "数码配件",
    "price" : 89,
    "quantity" : 36
}
product_2 = {
    "name" : "保温杯",
    "type" : "生活用品",
    "price" : 129,
    "quantity" : 18
}
product_3 = {
    "name" : "机械键盘",
    "type" : "数码配件",
    "price" : 399,
    "quantity" : 52
}
type_sales =  {}
current_sales = 0
products = [product_1,product_2,product_3]
for product in products:
    current_sales = product["price"] * product["quantity"]
    current_types = product["type"]
    if current_types in type_sales:
        type_sales[current_types] += current_sales
    else:
        type_sales[current_types] = current_sales
print(type_sales)