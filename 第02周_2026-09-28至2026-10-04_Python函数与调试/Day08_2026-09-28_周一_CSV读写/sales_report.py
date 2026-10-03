import csv

with open("Day08_2026-09-28_周一_CSV读写/products.csv", encoding="utf-8",newline="") as file:
    reader = csv.DictReader(file)
    with open("Day08_2026-09-28_周一_CSV读写/products_revenue.csv","w",encoding="utf-8",newline="")as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["name","current_sales"])
        for product in reader:
            current_price = float(product["price"])
            current_quantity = int(product["quantity"])
            current_sales = current_price * current_quantity
            writer.writerow([product["name"],current_sales])