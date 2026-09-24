def calculate_revenue(price,quantity):
    return price * quantity
revenue = calculate_revenue(25,40)
print(revenue)

def find_top_product(products):
    if not products:
        return None

    top_product = products[0]
    for product in products:
        if product["quantity"] > top_product["quantity"]:
            top_product = product
    return top_product

def find_top3_product(products):
    top3_product = sorted(
        products,
        key = lambda product : product["quantity"],
        reverse = True
    )
    return top3_product[:3]

def summarize_by_category(products):
    categorys_sales = {}
    for product in products:
        current_sales = calculate_revenue(product["price"],product["quantity"])
        current_category = product["category"]
        categorys_sales[current_category] = categorys_sales.get(current_category,0) + current_sales
    return categorys_sales

def find_top_revenue_product(products):
    if not products:
        return None

    top_revenue = 0
    top_revenue_product = products[0]
    for product in products:
        if calculate_revenue(product["price"],product["quantity"]) > top_revenue:
            top_revenue = calculate_revenue(product["price"],product["quantity"])
            top_revenue_product = product
    return top_revenue_product

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

new_products = [
    {"name": "水杯", "category": "生活用品", "price": 30, "quantity": 4},
    {"name": "笔记本", "category": "文具", "price": 12, "quantity": 7},
    {"name": "中性笔", "category": "文具", "price": 3, "quantity": 7},
]

zero_products = [
    {"name": "甲", "price": 10, "quantity": 0},
    {"name": "乙", "price": 20, "quantity": 0},
]

print(find_top_product(products))
print(find_top_product([]))

print(find_top3_product(products))
print(find_top3_product([]))

print(summarize_by_category(products))
print(summarize_by_category([]))

print(find_top_product(new_products))
print(summarize_by_category(new_products))

print(find_top_revenue_product(products))
print(find_top_revenue_product([]))

print(find_top_revenue_product(zero_products))