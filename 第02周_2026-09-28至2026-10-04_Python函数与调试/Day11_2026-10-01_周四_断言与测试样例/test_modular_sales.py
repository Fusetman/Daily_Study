from modular_sales import (
    validate_price,
    validate_quantity,
    validate_row,
    calculate_sales
)

def test_zero_quantity():
    product = {"price": "8","quantity": "0"}
    result = validate_row(product)

    assert result is not None
    assert calculate_sales(result) == 0

    print("零销量测试通过")

def test_normal_sales():
    product = {
        "price": "8",
        "quantity": "3"
    }
    result = validate_row(product)

    assert result is not None
    assert calculate_sales(result) == 24

    print("正常销量通过")

def test_invalid_price():
    product = {"price": "三十", "quantity": "3"}
    result = validate_row(product)

    assert result is None

    print("无效价格测试通过")

def test_valid_price():
    assert validate_price({"price": "8"}) == 8.0
    assert validate_price({"price": "0"}) == 0.0
    assert validate_price({"price": "2.5"}) == 2.5
    assert validate_price({"price": "-1"}) is None
    assert validate_price({"price": ""}) is None
    assert validate_price({}) is None

    print("价格校验通过")

def test_valid_quantity():
    assert validate_quantity({"quantity": "3"}) == 3
    assert validate_quantity({"quantity": "0"}) ==0
    assert validate_quantity({"quantity": "-1"}) is None
    assert validate_quantity({"quantity": "三"}) is None
    assert validate_quantity({"quantity": ""}) is None
    assert validate_quantity({}) is None

    print("销量校验通过")

def test_calculate_sales():
    assert calculate_sales({"price": 8.0, "quantity": 3}) == 24.0, "8 × 3 的销售额应为 24"
    assert calculate_sales({"price": 8.0, "quantity": 0}) == 0.0
    assert calculate_sales({"price": 0.0, "quantity": 3}) == 0.0

    print("销售额计算测试通过")

def test_decimal_sales():
    product = {"price": "2.5", "quantity": "4"}
    result = validate_row(product)

    assert result is not None
    assert calculate_sales(result) == 10

    print("小数校验通过")

if __name__ == "__main__":
    test_valid_price()
    test_valid_quantity()
    test_calculate_sales()
    test_zero_quantity()
    test_normal_sales()
    test_invalid_price()
    test_decimal_sales()
    print("全部测试通过")