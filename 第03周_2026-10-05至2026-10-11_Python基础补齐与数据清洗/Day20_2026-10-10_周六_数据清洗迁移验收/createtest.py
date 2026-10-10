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

    courses_pair = list(course_counts.items())
    sorted_courses = sorted(courses_pair,key=pair)

    return sorted_courses

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

course_records = [
    {"id": 201, "course": "Python", "hours": 2},
    {"id": 202, "course": "Python", "hours": 0},
    {"id": 203, "course": "SQL", "hours": 3},
    {"id": 201, "course": "SQL", "hours": 9},
]

# print(deduplicate(records))
# output(records,"Day20_2026-10-10_周六_数据清洗迁移验收/createtest01.csv")
# output(records_01,"Day20_2026-10-10_周六_数据清洗迁移验收/createtest02.csv")
# print(count_courses(course_records))
print(count_courses(course_records))