import csv

def reader(path):
    with open(path,encoding='utf-8',newline='')as file:
        reader = csv.DictReader(file)
        if reader == None:
            return None
        else:
            return list(reader)

# print(reader('Day37_2026-10-27_周二_销售项目边界补强/练习材料/快递签收独立小测/parcels.csv'))

def clean_rows(records):
    if records == None:
        return None

    packages = records.copy()
    for package in packages:
        for rows in package:
            package[rows] = package[rows].strip()

    return packages
records = reader('Day37_2026-10-27_周二_销售项目边界补强/练习材料/快递签收独立小测/parcels.csv')
# print(clean_rows(records))

def cleaned_rows(records):

    rejected = []
    output = {}
    duplicated = []
    kept_package = []
    valid = []
    clean_packages = clean_rows(records)
    for package in clean_packages:
        reasons = []
        invalid = {}
        duplicate_package = {}
        if 'package_id' not in package:
            reasons.append('没有编号')
        elif package['package_id'] is None or package['package_id'] == '':
            reasons.append('编号为空')

        if 'zone' not in package:
            reasons.append('没有配送区域')
        elif package['zone'] is None or package['zone'] == '':
            reasons.append('配送区域为空')

        if 'status' not in package:
            reasons.append('没有状态')
        elif package['status'] is None or package['status'] == '':
            reasons.append('状态为空')
        elif package['status'] not in ('signed','pending'):
            reasons.append('包裹状态不正确')

        if reasons != []:
            invalid['records'] = package
            invalid['reasons'] = reasons
            rejected.append(invalid)
        else:
            if package['package_id'] not in kept_package:
                valid.append(package)
                kept_package.append(package['package_id'])
            else:
                duplicate_package['records'] = package
                duplicated.append(package)

    output['valid'] = valid
    output['rejected'] = rejected
    output['duplicated'] = duplicated

    return output
def pair(pair):
    return (pair[1])

def rank_package(records):
    packages = {}
    for row in cleaned_rows(records)['valid']:
        packages[row['package_id']] = row['zone']
    sorted_packages = sorted(packages.items(),key=pair)

    return sorted_packages

def sign_rate(records):
    clean = cleaned_rows(records)['valid']
    zone_sign = {}
    sign_rate = {}
    zone_valid = {}
    for row in clean:
        print(row)
        current_zone = row['zone']
        current_sign = row['status']
        if current_sign == 'signed':
            zone_sign[current_zone] = zone_sign.get(current_zone,0) + 1
            zone_valid[current_zone] = zone_sign.get(current_zone,0) + 1
        else:
            zone_valid[current_zone] = zone_sign.get(current_zone,0) + 1


    print(zone_sign)
    print(zone_valid)

sign_rate(records)
def except_package(records,path):
    sorted = rank_package(records)
    sign = sign_rate(records)
    with open(path,'w',encoding='utf-8',newline='')as file:
        writer = csv.writer(file)
        writer.writerow(['zone','total','signed','sign_rate'])
        for row in rank_package(records):
            writer.writerow([row[1],sign[row[1]][0],sign[row[1]][1],sign[row[1]][0]])


print(rank_package(records))
print(cleaned_rows(records))
clean_test = cleaned_rows(records)
print(len(clean_test['valid']))
print(cleaned_rows([{'package_id': 'P009', 'zone': 'north', 'status': 'signed'}]))
assert len(clean_test['valid']) == 6
assert len(clean_test['rejected']) == 3
assert len(clean_test['duplicate']) == 0
