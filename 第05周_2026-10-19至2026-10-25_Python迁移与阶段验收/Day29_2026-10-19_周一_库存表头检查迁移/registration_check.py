import csv

def read_rows(path):
    records = []
    ori_names = ['registration_id','name','category','hours']
    lost = []
    with open(path,encoding='utf-8',newline='')as file:
        reader = csv.DictReader(file)
        for row in reader.fieldnames:
            if row not in ori_names:
                print(f'没有{row}')
                lost.append(row)
        if lost == []:
            return list(reader)
        else:
            return None

def num_clean(records):
    if

records = []
# print(read_rows('Day29_2026-10-19_周一_库存表头检查迁移/练习材料/registrations_weekly.csv'))
