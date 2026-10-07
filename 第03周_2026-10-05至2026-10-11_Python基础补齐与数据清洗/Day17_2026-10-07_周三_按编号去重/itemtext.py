tag_counts = {"python": 2, "sql": 3, "excel": 2}

pairs = list(tag_counts.items())
# print(pairs)

first = pairs[0]
# print(first)
# print(type(first))
# print(first[0])
# print(first[1])

def get_count(pair):
    return pair[1]

sorted_pairs = sorted(pairs,key=get_count,reverse=True)
# print(sorted_pairs)

def get_sort_key(pair):
    return (-pair[1],pair[0])

sorted_pairs02 = sorted(pairs,key=get_sort_key)
# print(sorted_pairs02)

for n in (2,5,0):
    top_tags = sorted_pairs02[:n]
    # print(top_tags)

empty_pairs = []
empty_sorted = sorted(empty_pairs, key=get_sort_key)
print(empty_sorted)
print(empty_sorted[:2])

new_counts = {"java": 2, "sql": 4, "go": 2, "python": 4}
pairs1 = list(new_counts.items())
sorted_counts = sorted(pairs1,key=get_sort_key)
print(sorted_counts[:3])