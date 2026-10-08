
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
    for fruit in records:
        if "id" not in fruit:
            print("没有id，无法判断")
            continue

        if fruit["id"] not in seed_ids:
            seed_ids[fruit["id"]] = True
            seed_fruit.append(fruit)

    return seed_fruit

records = ["SQL,Python", "Go,SQL", "Python"]
records_01 = [
    "SQL,sql,Go",
    "go,Python",
    "Python,Excel,excel",
    " ,SQL, "
]

records_02 = [
    {"id": 101, "name": "苹果"},
    {"id": 102, "name": "香蕉"},
    {"id": 101, "name": "橘子"},
    {"id": 103, "name": "葡萄"},
    {"id": 102, "name": "西瓜"}
]

records_03 = [
    {"id": 101, "name": "苹果"},
    {"id": 101, "name": "香蕉"},
    {"id": 101, "name": "橘子"},
]

records_04 = [
    {"id": 101, "name": "苹果"},
    {"id": 102, "name": "苹果"},
]

records_05 = [
    {"name": "梨"},
    {"id": 101, "name": "苹果"},
    {"id": 101, "name": "香蕉"},
]

count_tags(records)

assert count_tags([]) == {}
assert count_tags([""," , , "]) == {}
assert clean_tags(" SQL,Python,sql ") == ["sql", "python"]
assert count_tags(["SQL,Python", "Go,SQL", "Python"]) == {"sql": 2,"python": 2,"go": 1}
assert top_tags(count_tags(records),0) == []
assert top_tags(count_tags(records),5) == [('python',2),('sql',2),('go',1)]
assert top_tags(count_tags(records_01),3) == [('go',2),('python',2),('sql',2)]
assert deduplicate(records_02) == [{"id": 101, "name": "苹果"},{"id": 102, "name": "香蕉"},{"id": 103, "name": "葡萄"},]
assert deduplicate([]) == []
assert deduplicate(records_03) == [{"id": 101, "name": "苹果"}]
assert deduplicate(records_04) == [{"id": 101, "name": "苹果"},{"id": 102, "name": "苹果"}]
print(deduplicate(records_05))