import csv

headers = "Keyword,Monthly Average,Total Search,Quality Indice".split(",")

with open("final.csv") as file:
    rows = csv.DictReader(file)
    new_rows = sorted(rows, key=lambda row: float(row["Quality Indice"]))

with open("final_sorted.csv", "w") as file:
    writer = csv.DictWriter(file, headers)
    writer.writeheader()
    for row in new_rows:
        writer.writerow(row)
