rows = [
    {"registration_id": "001", "name": "小林"},
    {"registration_id": "002", "name": "小周"},
    {"registration_id": "003", "name": "小林"},
    {"registration_id": "001", "name": "小林"},
]

kept_ids = []
kept_rows = []
duplicate_rows = []

for msg in rows:
    if msg["registration_id"] in kept_ids:
        duplicate_rows.append(msg)
    else:
        kept_ids.append(msg["registration_id"])
        kept_rows.append(msg)

print(kept_rows)
print(duplicate_rows)