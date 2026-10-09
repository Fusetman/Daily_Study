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
    invalid_count = 0
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
        elif fruit["id"] == "" or fruit["id"] == " ":
            invalid["record"] = fruit
            invalid["reason"] = "编号无效"
            rejected.append(invalid)
            continue

        if fruit["id"] not in seed_ids:
            seed_ids[fruit["id"]] = True
            seed_fruit.append(fruit)

        else:
            duplicates.append(fruit)
    output["valid"] = seed_fruit
    output["rejected"] = rejected

    if len(seed_fruit) + len(duplicates) + len(rejected) == len(records):
        return output
    else:
        return None

def output(records,profile):
    cleaned_tags = deduplicate(records)
    valid_tag = cleaned_tags["valid"]
    invalid_tags = cleaned_tags["rejected"]
    with open(profile,"w",encoding="utf-8",newline="")as file:
        writer = csv.writer(file)
        writer.writerow(["id","name","status","reason"])
        for tag in valid_tag:
            writer.writerow([tag.get('id'),tag.get('name'),"valid",tag.get('reason')])
        for tag in invalid_tags:
            writer.writerow([(tag.get('record')).get('id'),(tag.get('record')).get('name'),"rejected",tag.get('reason')])

records = [
    {"name": "苹果"},
    {"id": None, "name": "香蕉"},
    {"id": 101, "name": "梨"},
]

print(deduplicate(records))
