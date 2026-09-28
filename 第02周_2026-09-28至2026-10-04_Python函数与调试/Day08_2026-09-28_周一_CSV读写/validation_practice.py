def validate_quantity(product):
    if "quantity" not in product:
        print("缺少销量字段")
        return None
    else:
        if product["quantity"] == "":
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


product = {
    "name": "橡皮",
    "price": "3",
    "quantity": "三"
}
result = validate_quantity(product)
print(result)