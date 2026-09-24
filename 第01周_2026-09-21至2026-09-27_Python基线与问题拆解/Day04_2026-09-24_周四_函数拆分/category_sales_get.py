product_01 = {
    "name" : "键盘",
    "category" : "数码配件",
    "price" : 120,
    "quantity" : 10
}
product_02 = {
    "name" : "鼠标",
    "category" : "数码配件",
    "price" : 60,
    "quantity" : 20
}
product_03 = {
    "name" : "毛巾",
    "category" : "生活用品",
    "price" : 20,
    "quantity" : 30
}
product_04 = {
    "name" : "数据线",
    "category" : "数码配件",
    "price" : 25,
    "quantity" : 40
}
product_05 = {
    "name" : "牙刷",
    "category" : "生活用品",
    "price" : 8,
    "quantity" : 50
}
products = [product_01,product_02,product_03,product_04,product_05]
category_sales = {}
for product in products:
    current_category = product["category"]
    current_sales = product["price"] * product["quantity"]
    category_sales[current_category] = category_sales.get(current_category,0) + current_sales
print(category_sales)