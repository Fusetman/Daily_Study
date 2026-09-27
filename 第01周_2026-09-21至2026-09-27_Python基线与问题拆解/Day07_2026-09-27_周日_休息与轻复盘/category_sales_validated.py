def summarize_by_category(products):
    if products == []:
        return {}

    category_sales = {}
    for product in products:
        current_sales = parse_revenue(product["revenue"])
        if current_sales is not None:
            current_category = product["category"]
            category_sales[current_category] = category_sales.get(current_category,0) + current_sales
    return category_sales

def parse_revenue(value):
    try:
        if float(value) >= 0:
            return float(value)
        else:
            return None
    except (ValueError,TypeError):
        return None

products = [
    {"name": "毛巾", "category": "日用品", "revenue": 60},
    {"name": "牙刷", "category": "日用品", "revenue": "40"},
    {"name": "笔", "category": "文具", "revenue": 30},
    {"name": "本子", "category": "文具", "revenue": 50},
    {"name": "水杯", "category": "日用品", "revenue": 0},
    {"name": "水杯", "category": "日用品", "revenue": "四十元"}
]
print(summarize_by_category(products))
print(summarize_by_category([]))
    
