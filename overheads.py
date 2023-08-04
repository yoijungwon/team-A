from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"Overheads.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    overheads = []
    for row in reader:
        overheads.append([row[0], row[1]])

# print(overheads)

def highest_oh():
    maximum = 0
    category = ""
    for item in overheads:
        item[1] = float(item[1])
        if item[1] > maximum:
            maximum = item[1]
            category += item[0]
    
    summary_report_o = ""   #create an empty string
    summary_report_o +=  "[HIGHEST OVERHEAD] " + str(category).upper() + ": " + str(maximum) + "%"

    with open("summary_report.txt", "w") as file:
        file.write(summary_report_o)
highest_oh()