registration_ids = ["001", "002", "003", "001", "004", "002"]
kept_ids = []
duplicate_ids = []

for num in registration_ids:
    if num in kept_ids:
        duplicate_ids.append(num)
    else:
        kept_ids.append(num)

print(kept_ids)
print(duplicate_ids)
