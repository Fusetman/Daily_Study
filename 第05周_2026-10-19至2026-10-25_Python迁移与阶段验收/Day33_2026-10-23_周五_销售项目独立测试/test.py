import csv
import math

def reader_sales(path):
    with open(path,encoding='utf-8',newline='')as file:
        reader = csv.DictReader(file)
        if reader == None:
            return None
        else:
            return list(reader)
# print(reader_sales('Day33_2026-10-23_周五_销售项目独立测试\sales.csv'))

def clean_row(records):
    if records == None:
        return None

    records_copy = records.copy()
    for row in records_copy:
        for rows in row:
            row[rows] = row[rows].strip()

    return records_copy
# print(cleaned_row(reader_sales('Day33_2026-10-23_周五_销售项目独立测试\sales.csv')))

def cleaned_row(records):
    if records == None:
            return None

    cleaned = clean_row(records)
    kept_id = []
    valid = []
    rejected = []
    duplicated = []
    output = {}
    for row in cleaned:
        invalid = {}
        reasons = []
        if 'line_id' not in row:
            reasons.append('没有编号')
        elif row['line_id'] == '' or row['line_id'] is None:
            reasons.append('编号为空')

        if 'product' not in row:
            reasons.append('没有商品名称')
        elif row['product'] == '' or row['product'] is None:
            reasons.append('商品名为空')

        if 'category' not in row:
            reasons.append('没有品类')
        elif row['category'] == '' or row['category'] is None:
            reasons.append('品类为空')

        if 'quantity' not in row:
            reasons.append('没有商品数量')
        elif row['quantity'] == '' or row['quantity'] is None:
            reasons.append('商品数量为空')
        try:
            quantity = int(row['quantity'])
            if quantity < 0:
                reasons.append('数量不能为负数')
            elif not math.isfinite(quantity):
                reasons.append('数量格式不正确')
        except ValueError:
            reasons.append('数量格式不正确')

        if 'unit_price' not in row:
            reasons.append('没有单价')
        elif row['unit_price'] == '' or row['unit_price'] is None:
            reasons.append('单价为空')
        try:
            unit_price = float(row['unit_price'])
            if unit_price < 0:
                reasons.append('单价不能为负数')
            elif not math.isfinite(unit_price):
                reasons.append('单价格式不正确')
        except ValueError:
            reasons.append('单价格式不正确')

        if reasons != []:
            invalid['records'] = row
            invalid['reasons'] = reasons
            rejected.append(invalid)
        else:
            if row not in kept_id:
                valid.append(row)
                kept_id.append(row['line_id'])
            else:
                duplicated.append(row)


    output['rejected'] = rejected
    output['valid'] = valid
    output['duplicated'] = duplicated
    return output

def summary_rows(records):
    rows = cleaned_row(records)
    category = {}
    product = {}
    for row in rows['valid']:
        quantity = int(row['quantity'])
        price = float(row['unit_price'])
        sum_sales=  quantity * price

        current_product = row['product']
        current_category = row['category']
        product[current_product] = product.get(current_product,0) + sum_sales
        category[current_category] = category.get(current_category,0) + sum_sales

    return [product,category]


def pair_product(pair):
    return (-pair[1],pair[0])

def pair_category(pair):
    return (pair[0],pair[1])

def rank_product(records):
    ranked_sum = []
    sum = summary_rows(records)[0]
    ranked_sum.append(sorted(sum.items(),key=pair_product))

    return ranked_sum[0]

def rank_category(records):
    ranked_sum = []
    sum = summary_rows(records)[1]
    ranked_sum.append(sorted(sum.items(),key=pair_category))

    return ranked_sum[0]

def average(records):
   product_counts = len(cleaned_row(records)['valid'])
   total_sales = 0
   for product in rank_product(records):
       total_sales += product[1]

   return total_sales / product_counts

def except_valid(records,path):
    with open(path,'w',encoding='utf-8',newline='')as file:
        writer = csv.writer(file)
        writer.writerow(['line_id','product','category','quantity','unit_price'])
        for row in cleaned_row(records)['valid']:
            writer.writerow([row['line_id'],row['product'],row['category'],row['quantity'],row['unit_price']])

def except_product(records,path):
    with open(path,'w',encoding='utf-8',newline='')as file:
        writer = csv.writer(file)
        writer.writerow(['product','total_sales'])
        for row in rank_product(records):
            writer.writerow([row[0],row[1]])

def except_category(records,path):
    with open(path,'w',encoding='utf-8',newline='')as file:
        writer = csv.writer(file)
        writer.writerow(['category','total_sales'])
        for row in rank_category(records):
            writer.writerow([row[0],row[1]])

def except_rejected(records,path):
    with open(path,'w',encoding='utf-8',newline='')as file:
        writer = csv.writer(file)
        writer.writerow(['line_id','product','category','quantity','unit_price','reasons'])
        for row in cleaned_row(records)['rejected']:
            writer.writerow([row['records']['line_id'],row['records']['product'],row['records']['category'],row['records']['quantity'],row['records']['unit_price'],row['reasons']])

records = reader_sales('Day33_2026-10-23_周五_销售项目独立测试/sales.csv')

# test = cleaned_row(records)
# assert len(test['valid']) == 11
# print(test['rejected'])
print(rank_product(records))
print(rank_category(records))
print(average(records))
# print(cleaned_row(records)['rejected'])
except_valid(records,'Day33_2026-10-23_周五_销售项目独立测试/valid.csv')
except_product(records,'Day33_2026-10-23_周五_销售项目独立测试/product.csv')
except_category(records,'Day33_2026-10-23_周五_销售项目独立测试/category.csv')
except_rejected(records,'Day33_2026-10-23_周五_销售项目独立测试/rejected.csv')
