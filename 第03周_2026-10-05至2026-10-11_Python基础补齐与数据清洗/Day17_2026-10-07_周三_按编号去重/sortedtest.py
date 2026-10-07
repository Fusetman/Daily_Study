def get_sort_key(pair):
    return (-pair[1],pair[0])

def top_tags(tag_counts, n):
    pair = list(tag_counts.items())
    sorted_tags = sorted(pair,key=get_sort_key)
    return sorted_tags[:n]

def clean_tags(tags):
    clean_langs = []
    for lang in tags.split(','):
        clean_lang = (lang.strip()).lower()
        if clean_lang != "" and clean_lang not in clean_langs:
            clean_langs.append(clean_lang)

    return clean_langs

def count_tags(records):
    tag_counts = {}

    for text in records:
        cleaned_tags = clean_tags(text)
        for tag in cleaned_tags:
            if tag not in tag_counts:
                tag_counts[tag] = tag_counts.get(tag,0) + 1
            else:
                tag_counts[tag] += 1

    return tag_counts

records = [
    " SQL,Python,sql ",
    "Go, python",
    "java,GO,",
    "",
    " , SQL, ",
    "Rust"
]


assert top_tags(count_tags(records),3) == [('go', 2), ('python', 2), ('sql', 2)]
print(top_tags(count_tags(records),3))
assert clean_tags(" SQL,Python,sql ") == ["sql", "python"]
assert clean_tags("") == []


assert top_tags({"java": 2, "sql": 4, "go": 2, "python": 4},3) == [('python', 4), ('sql', 4), ('go', 2)]
assert top_tags({"java": 2, "sql": 4, "go": 2, "python": 4},6) == [('python', 4), ('sql', 4), ('go', 2), ('java', 2)]
assert top_tags({},10) == []