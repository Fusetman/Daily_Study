product_01 = {
    "name" : "饼干",
    "category" : "食品",
    "price" : 9,
    "quantity" : 3
}
product_02 = {
    "name" : "笔",
    "category" : "文具",
    "price" : 5,
    "quantity" : 2
}
product_03 = {
    "name" : "面包",
    "category" : "食品",
    "price" : 4,
    "quantity" : 6
}
product_04 = {
    "name" : "本子",
    "category" : "文具",
    "price" : 3,
    "quantity" : 7
}
products = [product_01,product_02,product_03,product_04]

categorys_sales = {}
for product in products:
    current_category = product["category"]
    current_sales = product["price"] * product["quantity"]
    categorys_sales[current_category] = categorys_sales.get(current_category,0) + current_sales
print(categorys_sales)