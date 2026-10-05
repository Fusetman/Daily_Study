def validate_hours(row):
    if "hours" not in row or row["hours"] == "" or row["hours"] == None:
        return None
    else:
        try:
            hours = float(row["hours"])
            if hours < 0 :
                return None
            else:
                return hours
        except ValueError:
            return None

assert validate_hours({"hours": "2.5"}) == 2.5
assert validate_hours({"hours": "0"}) == 0.0
assert validate_hours({"hours": "-1"}) == None
assert validate_hours({"hours": ""}) == None
assert validate_hours({"hours": None}) == None
assert validate_hours({"hours": "abc"}) == None
assert validate_hours({}) == None

rows = [
    {"registration_id": "001", "name": "小林", "hours": "-1"},
    {"registration_id": "002", "name": "小周", "hours": "0"},
    {"registration_id": "001", "name": "小林", "hours": "2"},
    {"registration_id": "001", "name": "小林", "hours": "3"},
    {"registration_id": "003", "name": "小陈", "hours": "abc"},
]

kept_ids = []
kept_rows = []
invalid_rows = []
duplicate_rows = []

for row in rows:
    hours = validate_hours(row)
    if hours is None:
        invalid_rows.append(row)
    else:
        if row["registration_id"] in kept_ids:
            duplicate_rows.append(row)
        else:
            kept_ids.append(row["registration_id"])
            kept_rows.append(row)

if len(rows) == len(invalid_rows) + len(duplicate_rows) + len(kept_rows):
    print(f'共{len(rows)}条，条数检验合格')

print(invalid_rows)
print(kept_rows)
print(duplicate_rows)