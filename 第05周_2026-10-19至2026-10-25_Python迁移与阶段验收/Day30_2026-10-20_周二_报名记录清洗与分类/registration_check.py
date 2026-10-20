import csv

def read_rows(path):
    records = []
    ori_names = ['registration_id','name','category','hours']
    lost = []
    with open(path,encoding='utf-8',newline='')as file:
        reader = csv.DictReader(file)
        records = list(reader)
        for row in reader.fieldnames:
            if row not in ori_names:
                print(f'没有{row}')
                lost.append(row)
        if lost == []:
            return records
        else:
            return None
# print(read_rows('Day30_2026-10-20_周二_报名记录清洗与分类/练习材料/registrations_weekly.csv'))
def clean_rows(records):
    if records is None or records == []:
        return None
    cleaned_records =  []
    for row in records:
        for rows in row:
            row[rows] = row[rows].strip()
        cleaned_records.append(row)
    return cleaned_records


def cleaned_rows(records):
    if records is None or records == []:
        return None

    rows = clean_rows(records)
    valid = []
    rejected = []
    output = {}
    for row in rows:
        invalid = {}
        reasons = []
        kept_row = []
        duplicate = []
        if 'registration_id' not in row:
            reasons.append("没有编号")
        elif row['registration_id'] == '' or row['registration_id'] is None:
            reasons.append('编号为空')
        else:
            try:
                test_id = int(row['registration_id'])
                if test_id < 0 or test_id == 0 :
                    reasons.append('编号格式错误')
            except (TypeError,ValueError):
                reasons.append('编号格式错误')
            if  row['registration_id'] not in kept_row:
                kept_row.append(row['registration_id'])
            else:
                reasons.append("编号重复")
                duplicate.append(row)

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
            except (KeyError,ValueError):
                reasons.append('时长格式不正确')
        if reasons != []:
            invalid['records'] = row
            invalid['reasons'] = reasons
            rejected.append(invalid)
        else:
            valid.append(row)
    output['valid'] = valid
    output['rejected'] = rejected
    output['duplicate'] = duplicate
    return output

def pair_rank(pair):
    return (pair[1],pair[0])

def rank_rows(records):
    if records is None or records == []:
        return None

    rows = cleaned_rows(records)['valid']
    total_hours = {}
    for row in rows:
        current_catrgory = row['category']
        current_hours = float(row['hours'])
        if current_catrgory not in total_hours:
            total_hours[current_catrgory] = total_hours.get(current_catrgory,0) + current_hours
        else:
            total_hours[current_catrgory] += total_hours.get(current_catrgory,0) + current_hours
        # total_hours[current_catrgory] = str(total_hours[current_catrgory])
    for row in total_hours.items():
        print(row)

def except_row(record,path):
    if records is None or records == []:
        return None
    rows = cleaned_rows(record)['valid']
    with open(path,'w',encoding='utf-8',newline='')as file:
        writer = csv.writer(file)
        writer.writerow(['registration_id','name','category','hours'])
        for row in rows:
            writer.writerow([row['registration_id'],row['name'],row['category'],row['hours']])
    # print(ranked)

records = read_rows('Day30_2026-10-20_周二_报名记录清洗与分类/练习材料/registrations_weekly.csv')
print(cleaned_rows(records))
except_row(records,'Day30_2026-10-20_周二_报名记录清洗与分类/练习材料/output.csv')
# print(cleaned_rows(records))
# def rank_rows(records):



# clean_rows(records)
#print(read_rows('Day30_2026-10-20_周二_报名记录清洗与分类/练习材料/registrations_weekly.csv'))
