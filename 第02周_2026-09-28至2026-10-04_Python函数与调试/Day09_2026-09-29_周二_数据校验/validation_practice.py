import csv

def validate_quantity(product):
    if "quantity" not in product:
        print("缺少销量字段")
        return None
    else:
        if product["quantity"] in ("",None):
            print("销量为空")
            return None
        else:
            try:
                quantity = int(product["quantity"])
                if quantity < 0:
                    print("销量为负数")
                    return None
                else:
                    return quantity
            except ValueError:
                print("销量无法转换")
                return None

def validate_price(product):
    if "price" not in product:
        print("缺少price数据")
        return None
    else:
        if product["price"] in ("",None):
            print("销售单价不存在")
            return None
        try:
            price = float(product["price"])
            if price < 0:
                print("售价为负数")
                return None
            else:
                return price
        except ValueError:
            print("售价无法转换")
            return None

def validate_row(product):
    price = validate_price(product)
    quantity = validate_quantity(product)
    if price == None or quantity == None:
        return None
    else:
        product["price"] = price
        product["quantity"] = quantity
    return product

def calculate_sales(product):
    return product["price"] * product["quantity"]


product_1 = {
    "name": "橡皮",
    "price": "3",
    "quantity": "3"
}
product_2 = {
    "name": "橡皮",
    "price": "19.9",
    "quantity": "3"
}
product_3 = {
    "name": "橡皮",
    "price": "三元",
    "quantity": "-3"
}
product_4 = {
    "name": "橡皮",
    "price": "-1",
    "quantity": "19.9"
}

# result = validate_row(product_1)
# result03 = validate_row(product_3)
# result04 = validate_row(product_4)
# print(result03)
# print(result04)
# print(result)

# for product in [product_1,product_3,product_4]:
#     result = validate_row(product)
#     if result == None:
#         print("跳过")
#         print(product)
#     else:
#         print(result)

with open("Day09_2026-09-29_周二_数据校验/products_test.csv","w",encoding="utf-8",newline="")as file:
    writer = csv.writer(file)
    writer.writerow(["name","category","price","quantity"])
    writer.writerow(["毛巾", "日用品", "19.9", "3"])
    writer.writerow(["牙刷", "日用品", "8", "0"])
    writer.writerow(["笔", "文具", "2", "5"])
    writer.writerow(["杯子", "日用品", "三十", "2"])
    writer.writerow(["橡皮", "文具", "-1", "4"])
    writer.writerow(["文件夹", "文具", "12", "两个"])
    writer.writerow(["胶带", "文具", "5", "-2"])
    writer.writerow(["本子", "文具", "", "3"])
    writer.writerow(["尺子", "文具", "3", ""])
    writer.writerow(["缺销量商品", "文具", "9"])
with open("Day09_2026-09-29_周二_数据校验/products_test.csv",encoding="utf-8",newline="")as file:
    reader = csv.DictReader(file)
    for product in reader:
        result = validate_row(product)
        if result == None:
            print("跳过")
            print(product)
        else:
            print(result)
            print(calculate_sales(result))
