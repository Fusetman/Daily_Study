import csv

def read_inventory(path):
    with open(path,encoding="utf-8",newline="")as file:
        reader = csv.DictReader(file)
        return list(reader)

def write_summary(path,category_totals):
    with open(path,"w",encoding="utf-8",newline="")as file:
        writer = csv.writer(file)
        writer.writerow(["category","total_value"])
        for category,total_value in category_totals.items():
            writer.writerow([category,f'{total_value:.2f}'])

def validate_price(product):
    if "price" not in product:
        print("没有单价")
        return None
    else:
        if product["price"] == "" or product["price"] is None:
            print("单价不能为空")
            return None
        try:
            price = float(product["price"])
            if price < 0 :
                print("单价不能为负数")
                return None
            else:
                return price
        except ValueError:
            print("单价无法转换")
            return None

def validate_quantity(product):
    if "quantity" not in product:
        print("没有库存")
        return None
    else:
        if product["quantity"] == "" or product["quantity"] is None:
            print("库存不能为空")
            return None
        try:
            quantity = int(product["quantity"])
            if quantity < 0 :
                print("库存不能为负数")
                return None
            else:
                return quantity
        except ValueError:
            print("库存无法转换")
            return None

def validate_rows(product):
    if "product" not in product or product["product"] is None or product["product"] == "":
        print("商品数据不能为空")
        return None
    elif "category" not in product or product["category"] is None or product["category"] == "":
        print("品类不能为空")
        return None
    else:
        price = validate_price(product)
        quantity = validate_quantity(product)
        if price is None or quantity is None:
            return None
        else:
            product["price"] = price
            product["quantity"] = quantity
            return product

def summarize_inventory(rows):
    category_totals = {}
    for product in rows:
        current_category = product["category"]
        current_total = product["price"] * product["quantity"]
        category_totals[current_category] = category_totals.get(current_category,0) + current_total
    return category_totals

# rows = [
#     {"category": "文具", "price": 12.5, "quantity": 4},
#     {"category": "文具", "price": 2.0, "quantity": 10},
#     {"category": "日用品", "price": 25.0, "quantity": 3},
# ]

# zero_rows = [
#     {"category": "文具", "price": 8.0, "quantity": 0}
# ]

# print(summarize_inventory(rows))
# print(summarize_inventory(zero_rows))
# print(read_inventory("Day13_2026-10-03_周六_库存分析周测/inventory.csv"))

# assert summarize_inventory([]) == {}
# assert summarize_inventory(zero_rows) == {"文具": 0.0}

# test_cases = [
#     {"input": {"price": "12.5"}, "expected": 12.5},
#     {"input": {"price": "0"}, "expected": 0.0},
#     {"input": {"price": "-1"}, "expected": None},
# ]

# for product in test_cases:
#     assert validate_price(product["input"]) == product["expected"] , product["input"]
# assert validate_price({"price": "十五"}) is None
# assert validate_price({"price": ""}) is None
# assert validate_price({"price": None}) is None
# assert validate_price({}) is None

# assert validate_quantity({"quantity": "4"}) == 4
# assert validate_quantity({"quantity": "0"}) == 0
# assert validate_quantity({"quantity": "2.5"}) is None
# assert validate_rows({
#     "product": "收纳盒",
#     "category": "日用品",
#     "price": "18",
#     "quantity": "-1"
# }) is None

products = read_inventory("Day13_2026-10-03_周六_库存分析周测/inventory.csv")
valid_rows = []
valid_count = 0
invalid_count = 0
total_sales = 0
for product in products:
    row = validate_rows(product)
    if not row is None:
        valid_count += 1
        valid_rows.append(row)
    else:
        invalid_count += 1

category_totals = summarize_inventory(valid_rows)

for category,sales in category_totals.items():
    total_sales += sales

print(category_totals)
print(f'库存总金额：{total_sales:.2f}')
print(f'有效{valid_count}条，无效{invalid_count}条')
write_summary(
    "Day13_2026-10-03_周六_库存分析周测/summary_inventory.csv",
    category_totals
    )
