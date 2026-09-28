import csv

with open("Day08_2026-09-28_周一_CSV读写/sales_output.csv","w",encoding="utf-8",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name","revenue"])
    writer.writerow(["毛巾",59.7])