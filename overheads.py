from pathlib import Path
import csv

#create a file to csv file.
fp = Path.cwd()/"csv_reports"/"Overheads.csv"

#read the csv file to append category and overhead from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) #skip header

    #create an emply list to store the percentage of the different categories of overheads
    overheads = []

    #append categories and overheads into the overheads list
    for row in reader:
        #get the categories and overheads
        #and append overheads list
        overheads.append([row[0], row[1]])

# print(overheads)

def highest_oh():
    """
    Find the highest overhead.
    Parameters are not required.
    """

    maximum = 0 #create a variable named maximum and assign as 0
    category = "" #create a string to store the category which has the highest overhead
    for item in overheads:
        #iterate each row of data in overheads list
        #typecast overheads into floats
        item[1] = float(item[1])
        if item[1] > maximum: 
            maximum = item[1] #assign the highest overhead from the overheads list to maximum
            category += item[0] #add the highest overhead's category into list
    
    summary_report_o = ""   #create an empty string
    summary_report_o +=  "[HIGHEST OVERHEAD] " + str(category).upper() + ": " + str(maximum) + "%"

    with open("summary_report.txt", "w") as file:
        file.write(summary_report_o)
highest_oh()