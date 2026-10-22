import csv
import math

def read_rows(path):
    records = []
    ori_names = ['registration_id','name','category','hours']
    lost = []
    with open(path,encoding='utf-8',newline='')as file:
        reader = csv.DictReader(file)
        records = list(reader)
        if reader.fieldnames is None:
            print('没有表头')
            return None
        else:
            for row in ori_names:
                if row not in reader.fieldnames:
                    print(f'没有{row}')
                    lost.append(row)
        if lost == []:
            return records
        else:
            return None

read_rows('Day32_2026-10-22_周四_报名记录断言与复盘/练习材料/registrations_weekly.csv')

def clean_rows(records):
    if records is None:
        return None
    cleaned_records =  []
    for row in records:
        for rows in row:
            if isinstance(row[rows],str):
                row[rows] = row[rows].strip()
        cleaned_records.append(row)

    return cleaned_records


def cleaned_rows(records):
    if records is None:
        return None

    rows = clean_rows(records)
    valid = []
    rejected = []
    output = {}
    kept_row = []
    duplicate = []
    for num, row in enumerate(rows, start=2):
        invalid = {}
        reasons = []
        duplicate_row = {}

        if 'registration_id' not in row:
            reasons.append("没有编号")
        elif row['registration_id'] == '' or row['registration_id'] is None:
            reasons.append('编号为空')

        if 'name' not in row:
            reasons.append('姓名不存在')
        elif row['name'] is None or row['name'] == '':
            reasons.append('姓名为空')
        elif not isinstance(row['name'],str):
                reasons.append('姓名格式不正确')

        if 'category' not in row:
            reasons.append('类别不存在')
        elif row['category'] is None or row['category'] == '':
            reasons.append('类别为空')
        elif not isinstance(row['category'],str):
            reasons.append('类别格式不正确')

        if 'hours' not in row:
            reasons.append('没有时间')
        elif row['hours'] is None or row['hours'] == '':
            reasons.append('时长为空')
        else:
            try:
                hours = float(row['hours'])
                if hours < 0:
                    reasons.append('时长为负数')
                elif not math.isfinite(hours):
                    reasons.append('时长格式不正确')
            except (KeyError,ValueError):
                reasons.append('时长格式不正确')

        if reasons != []:
            invalid['records'] = row
            invalid['reasons'] = reasons
            invalid['line'] = num
            rejected.append(invalid)
        else:
            if row['registration_id'] not in kept_row:
                valid.append(row)
                kept_row.append(row['registration_id'])
            else:
                duplicate_row['record'] = row
                duplicate_row['reasons'] = "编号重复"
                duplicate_row['line'] = num
                duplicate.append(duplicate_row)


    output['valid'] = valid
    output['rejected'] = rejected
    output['duplicate'] = duplicate

    return output


def pair_rank(pair):
    return (-pair[2],pair[0])

def summary_rows(records):
    if records is None:
        return None

    rows = cleaned_rows(records)['valid']
    total_hours = {}
    count_category = {}
    summarize = []
    for row in rows:
        current_category = row['category']
        current_hours = float(row['hours'])
        if current_category not in total_hours:
            total_hours[current_category] = total_hours.get(current_category,0) + current_hours
            count_category[current_category] = count_category.get(current_category,0) + 1
        else:
            total_hours[current_category] += current_hours
            count_category[current_category] += 1


    for category,count in count_category.items():
        summarize.append((category,count,total_hours[category]))

    return sorted(summarize,key=pair_rank)

def except_row(record,path):
    if record is None:
        return None
    rows = cleaned_rows(record)['valid']
    with open(path,'w',encoding='utf-8',newline='')as file:
        writer = csv.writer(file)
        writer.writerow(['registration_id','name','category','hours'])
        for row in rows:
            writer.writerow([row['registration_id'],row['name'],row['category'],row['hours']])
    # print(ranked)
def except_summary(records,path):
    if records is None:
        return None

    rows = summary_rows(records)
    with open(path,'w',encoding='utf-8',newline='')as file:
        writer = csv.writer(file)
        writer.writerow(['category','count','total_hours'])
        for row in rows:
            writer.writerow([row[0],row[1],row[2]])

# records = read_rows('Day32_2026-10-22_周四_报名记录断言与复盘/练习材料/registrations_weekly.csv')
records = [
    {'registration_id': 'R001', 'name': '李红','category': 'B','hours': '2'},
    {'registration_id': 'R002', 'name': '李黄','category': 'A','hours': '1'},
    {'registration_id': 'R003', 'name': '李蓝','category': 'A','hours': '1'},
    {'registration_id': 'R004', 'name': '李绿','category': 'C','hours': '3'}
]

test = summary_rows(records)
print(test)
assert test == [('C', 1, 3.0), ('A', 2, 2.0), ('B', 1, 2.0)]
# test = cleaned_rows(records)
# print(test)
# assert test['valid'][0]['hours'] == '2'
# assert test['rejected'][0]['line'] == 2
# assert test['duplicate'][0]['line'] == 4
# print(summary_rows(records))
# except_summary(records,'Day32_2026-10-22_周四_报名记录断言与复盘/练习材料/summary.csv')
# print(cleaned_rows(records))
# print(cleaned_rows(records))
# test = cleaned_rows(records)
# print(test)
# print(len(records))
# assert len(test['valid']) == 8
# assert len(test['rejected']) == 8
# assert len(test['duplicate']) == 2
# assert len(test['valid']) + len(test['rejected']) + len(test['duplicate']) == len(records)
# except_row(records,'Day32_2026-10-22_周四_报名记录断言与复盘/练习材料/output.csv')
# print(cleaned_rows(records))



# clean_rows(records)
#print(read_rows('Day30_2026-10-20_周二_报名记录清洗与分类/练习材料/registrations_weekly.csv'))
