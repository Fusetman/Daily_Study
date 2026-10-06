text = " Python ,PYTHON, SQL,sql,,Excel, "

def clean_tags(text):
    cleaned_text = []
    kept_text= []
    duplicate_text = []
    for lang in text.split(','):
        cleaned_lang = (lang.strip()).lower()
        if cleaned_lang not in cleaned_text and not cleaned_lang == "":
            cleaned_text.append(cleaned_lang)
        else:
            duplicate_text.append(cleaned_lang)

    return cleaned_text

assert clean_tags(" Python ,PYTHON, SQL,sql,,Excel, ") == [
    "python", "sql", "excel"
]
assert clean_tags("") == []
assert clean_tags(" , , ") == []
assert clean_tags("SQL") == ["sql"]
records = [
    " Python,SQL,python ",
    "sql, Excel",
    "Python,,excel,EXCEL",
    "",
    " , , ",
    "SQL",
    "Go"
]

tag_counts = {}
for record in records:
    clean_record = clean_tags(record)
    for lang in clean_record:
        tag_counts[lang] = tag_counts.get(lang,0) + 1

print(tag_counts)