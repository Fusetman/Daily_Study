import csv

with open("Day08_2026-09-28_周一_CSV读写/products.csv", encoding="utf-8",newline="") as file:
    reader = csv.DictReader(file)
    for product in reader:
        current_price = float(product["price"])
        current_quantity = int(product["quantity"])
        current_sales = current_price * current_quantity
        print(f'{product["name"]}的总销售额为{current_sales}')