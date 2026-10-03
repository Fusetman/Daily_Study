import csv

DATA_PATH = "Day09_2026-09-29_周二_数据校验/products_test.csv"

def read_product(file_path):
    product = []
    with open (file_path,encoding="utf-8",newline="")as file:
        reader = csv.DictReader(file)
        for result in reader:
            product.append(result)
        return product

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

def display_sales(name,sales):
    print(f"商品名称为：{name}，商品销售额为：{sales:.2f}")

def display_summary(total_sales,valid_count,invalid_count):
    print(f'有效商品的总销售额为：{total_sales:.2f}')
    print(f'有效商品一共有{valid_count}个')
    print(f'无效商品一共有{invalid_count}个')

def main():
    product = read_product(DATA_PATH)
    total_sales = 0
    valid = 0
    invalid = 0
    for result in product:
        result_valdt = validate_row(result)
        if result_valdt == None:
            invalid += 1
            continue
        else:
            valid += 1
            sales = calculate_sales(result_valdt)
            display_sales(result_valdt["name"],sales)
            total_sales += sales
    display_summary(total_sales,valid,invalid)



if __name__ =="__main__":
    main()
