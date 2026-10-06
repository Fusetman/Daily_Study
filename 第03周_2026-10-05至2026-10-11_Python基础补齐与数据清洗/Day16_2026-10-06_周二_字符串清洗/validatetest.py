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

sample = {"hours": "2"}
converted_hours = validate_hours(sample)

# print(converted_hours)
# print(type(converted_hours))

# print(sample["hours"])
# print(type(sample["hours"]))

# cleaned = sample.copy()
# cleaned["hours"] = converted_hours

# print(sample)
# print(type(sample["hours"]))
# print(cleaned)
# print(type(cleaned["hours"]))

row = {
    "registration_id": "008",
    "name": "小林",
    "hours": "1.5"
}

hours = validate_hours(row)
cleaned_row = row.copy()
cleaned_row["hours"] = hours
print(row)
print(type(row["hours"]))
print(cleaned_row)
print(type(cleaned_row["hours"]))