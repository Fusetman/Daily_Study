import csv

def clean_tags(text):
    clean_langs = []
    for row in text.split(","):
        cleaned_row = (row.strip()).lower()
        if cleaned_row != "" and cleaned_row not in clean_langs:
            clean_langs.append(cleaned_row)
    return clean_langs

def count_tags(records):
    tag_counts = {}

    for text in records:
        cleaned_text = clean_tags(text)
        for tag in cleaned_text:
            tag_counts[tag] = tag_counts.get(tag,0) + 1

    return tag_counts

def pair_sorted(pair):
    return (-pair[1],pair[0])

def top_tags(tag_counts,n):
    tags_pairs = list(tag_counts.items())
    tags_sorted = sorted(tags_pairs,key=pair_sorted)

    return tags_sorted[:n]

def deduplicate(records):
    seed_ids = {}
    seed_fruit = []
    output = {}
    rejected = []
    duplicates = []

    for fruit in records:
        invalid = {}
        if "id" not in fruit:
            invalid["record"] = fruit
            invalid["reason"] = "缺少编号"
            rejected.append(invalid)
            continue
        elif fruit["id"] == None:
            invalid["record"] = fruit
            invalid["reason"] = "编号为None"
            rejected.append(invalid)
            continue
        elif isinstance(fruit["id"],str) and fruit["id"].strip() == "":
            invalid["record"] = fruit
            invalid["reason"] = "编号无效"
            rejected.append(invalid)
            continue

        duplicates_rows = {}
        if fruit["id"] not in seed_ids:
            seed_ids[fruit["id"]] = True
            seed_fruit.append(fruit)

        else:
            duplicates_rows["record"] = fruit
            duplicates_rows["reason"] = "编号重复"
            duplicates.append(duplicates_rows)
            continue


    output["valid"] = seed_fruit
    output["rejected"] = rejected
    output["duplicated"] = duplicates

    if len(seed_fruit) + len(duplicates) + len(rejected) == len(records):
        return output
    else:
        return None

def output(records,profile):
    cleaned_tags = deduplicate(records)
    if cleaned_tags == None:
        print("条数核对失败，未导出")
        return None


    valid_tag = cleaned_tags["valid"]
    invalid_tags = cleaned_tags["rejected"]
    duplicate_tag = cleaned_tags["duplicated"]
    with open(profile,"w",encoding="utf-8",newline="")as file:
        writer = csv.writer(file)
        writer.writerow(["id","name","status","reason"])
        for tag in valid_tag:
            writer.writerow([tag.get('id'),tag.get('name'),"valid",tag.get('reason')])
        for tag in invalid_tags:
            writer.writerow([(tag.get('record')).get('id'),(tag.get('record')).get('name'),"rejected",tag.get('reason')])
        for tag in duplicate_tag:
            writer.writerow([(tag.get('record')).get('id'),(tag.get('record')).get('name'),"duplicated",tag.get('reason')])

def count_courses(valid_records):
    if valid_records == None:
        print("条数核对失败，未导出")
        return None

    clean_courses = deduplicate(valid_records)
    valid_courses = clean_courses['valid']
    kept_courses = []
    output_courses = {}
    for tag in valid_courses:
        current_course = tag['course']
        current_hours = tag['hours']
        if current_course not in kept_courses:
            counted_courses = {}
            counted_courses["count"] = counted_courses.get("count",0) + 1
            counted_courses["total_hours"] = counted_courses.get("total_hours",0) + current_hours
            kept_courses.append(current_course)
        else:
            counted_courses = output_courses[current_course]
            counted_courses["count"] += 1
            counted_courses["total_hours"] += current_hours
        output_courses[current_course] = counted_courses

    return output_courses


def pair(pair):
    return [-pair[1],pair[0]]


def rank_course(course_counts):
    if course_counts == None:
        print("报名列表错误，请检查后传入")
        return None

    courses_done = {}
    sorted_courses = []
    for course in course_counts:
        courses_done[course] = course_counts[course]["total_hours"]
    courses_list = list(courses_done.items())
    sorted_courses = sorted(courses_list,key=pair)

    return sorted_courses

def except_courses(course_counts,filename):
    if course_counts == None:
        return None
    counted_course = rank_course(course_counts)
    with open(filename,"w",encoding="utf-8",newline="")as file:
        writer = csv.writer(file)
        writer.writerow(["course","count","total_hours"])
        for course in counted_course:
            writer.writerow([course[0],course_counts[course[0]]['count'],course[1]])

def validate_courses(records):
    if records == None:
        return None
    if records == []:
        return {"valid": [], "rejected": []}

    output_courses = {}
    valid = []
    rejected = []
    invalid = {}
    for record in records:
        invalid = {}
        reasons = []
        if 'course' not in record or record['course'] == None :
            reasons.append("没有课程")
        elif not isinstance(record['course'],str):
            reasons.append('课程格式不正确')
        elif record['course'].strip() == '':
            reasons.append("课程为空")

        if 'hours' not in record or record['hours'] == None:
            reasons.append("没有时长")

        else:
            if type(record['hours']) not in (int,float) or record['hours'] < 0:
                reasons.append("时长格式不正确")

        if reasons:
            invalid["record"] = record
            invalid["reason"] = "；".join(reasons)
            rejected.append(invalid)
        else:
            record_copy = record.copy()
            record_copy["course"] = record["course"].strip()
            valid.append(record_copy)

    output_courses["valid"] = valid
    output_courses["rejected"] = rejected

    return output_courses

def cleaned_records(records):
    clean_courses = validate_courses(records)
    if clean_courses == None:
        return None

    valid = clean_courses['valid']
    rejected = clean_courses['rejected']
    output = deduplicate(valid)
    counted_valid = count_courses(output['valid'])
    output['rejected'] = output['rejected'] + rejected
    return {'汇总结果' : counted_valid,
            '清洗结果': output}

def read_courses(path):
    with open(path,encoding='utf-8',newline='')as file:
        reader = csv.DictReader(file)
        if reader.fieldnames == None:
            print('没有表头')
            return None
        for name in ['id', 'course', 'hours']:
            if name not in reader.fieldnames:
                print(f'缺少表头{name}')
                return None

        return list(reader)

print(read_courses("第04周_2026-10-12至2026-10-18_销售分析项目/Day24_2026-10-14_周三_核心指标/courses.csv"))

records = [
    {"id": 501, "course": "SQL", "hours": -1},
    {"id": 501, "course": "SQL", "hours": 2},
    {"course": "Python", "hours": 1},
    {"id": 502, "course": " Python ", "hours": 3},
    {"id": 503, "course": "SQL", "hours": 1},
    {"id": 501, "course": "Excel", "hours": 9},
]

summary = cleaned_records(records)
except_courses(summary['汇总结果'],"第04周_2026-10-12至2026-10-18_销售分析项目/Day24_2026-10-14_周三_核心指标/course_summary.csv")
print(f'排名结果：{rank_course(summary['汇总结果'])}')
assert len(summary['清洗结果']['valid']) + len(summary['清洗结果']['rejected']) + len(summary['清洗结果']['duplicated']) == len(records)
hours = 0
total_hours = 0
for course in summary['清洗结果']['valid']:
    hours += course['hours']
for course in summary['汇总结果'].items():
    total_hours += course[1]['total_hours']
assert hours == total_hours
# records = [
#     {"id": 401, "course": " Python ", "hours": 2},
#     {"id": 402, "course": "SQL", "hours": 0},
#     {"id": 403, "course": "Excel", "hours": 1.5},
#     {"id": 404, "course": "SQL", "hours": -1},
#     {"id": 405, "course": "SQL", "hours": "2"},
#     {"id": 406, "course": "SQL", "hours": None},
#     {"id": 407, "course": "SQL"},
#     {"id": 407,},
#     {"id": 408, "hours": 2},
#     {"id": 409, "course": 123, "hours": 2}
# ]

# print(validate_courses(records))
# print(validate_courses([]))
# records = [
#     {"name": "苹果"},
#     {"name": "榴莲"},
#     {"id": None, "name": "香蕉"},
#     {"id": 101, "name": "梨"},
#     {"id": 101, "name": "橘子"},
#     {"id": 101, "name": "桃子"}
# ]

# records_01 = [
#     {"id": " ", "name": "香蕉"},
#     {"id": "\t", "name": "王钰晖"},
#     {"id": 0, "name": "华为"},
# ]

# course_records = [
#     {"id": 201, "course": "Python"},
#     {"id": 202, "course": "SQL"},
#     {"id": 203, "course": "Python"},
#     {"id": 201, "course": "SQL"},
#     {"id": 204, "course": "SQL"},
#     {"id": 205, "course": "Python"},
# ]

# course_records = [
#     {"id": 201, "course": "Python", "hours": 2},
#     {"id": 202, "course": "Python", "hours": 0},
#     {"id": 203, "course": "SQL", "hours": 3},
#     {"id": 201, "course": "SQL", "hours": 9},
# ]

# print(deduplicate(records))
# output(records,"Day20_2026-10-10_周六_数据清洗迁移验收/createtest01.csv")
# output(records_01,"Day20_2026-10-10_周六_数据清洗迁移验收/createtest02.csv")
# print(count_courses(course_records))
# print(count_courses(course_records))
# print(rank_course(count_courses(course_records)))
# except_courses(count_courses(course_records),"第04周_2026-10-12至2026-10-18_销售分析项目/Day23_2026-10-13_周二_读取与清洗/course_summary.csv")
