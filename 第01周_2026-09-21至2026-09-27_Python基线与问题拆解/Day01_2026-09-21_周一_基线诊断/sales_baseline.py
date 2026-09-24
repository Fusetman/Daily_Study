product_1 = {
    "name": "毛巾",
    "category": "家居用品",
    "price": 19.9,
    "quantity": 100
}
product_2 = {
    "name": "牙刷",
    "category": "家居用品",
    "price": 5,
    "quantity": 200
}
product_3 = {
    "name": "牙膏",
    "category": "家居用品",
    "price": 30,
    "quantity": 300
}
product_4 = {
    "name": "湿巾",
    "category": "清洁用品",
    "price": 6,
    "quantity": 150
}
product_5 = {
    "name": "纸巾",
    "category": "清洁用品",
    "price": 4,
    "quantity": 170
}
product_6 = {
    "name": "护发精油",
    "category": "个人护理",
    "price": 40,
    "quantity": 30
}
products = [product_1,product_2,product_3,product_4,product_5,product_6]
total_sales = 0
for product in products:
    total_sales += product["price"]*product["quantity"]
print (total_sales)
average_sales = total_sales / len(products)
print(average_sales)
max_sales = 0
max_product = ""
for product in products:
    current_sale = product["price"]*product["quantity"]
    if current_sale > max_sales:
        max_sales = current_sale
        max_product = product["name"]
print(max_sales)
print(max_product)
#输入：一个商品列表，每个商品包含名称，品类，单价和销量
#输出：输出了产品的总销售额，平均销售额，销售额最高的商品名称以及销售额
#计算规则：销售额 = 价格 * 数量  平均销售额 = 总销售额 / 商品数量
#处理步骤：先计算总销售额，再计算平均销售额，最后遍历商品查找销售额最高的产品名称