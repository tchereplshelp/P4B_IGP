from pathlib import Path
import csv

# create a file path to csv file in the subfolder named "csv_reports"
subfolder_name = "csv_reports"
fp = Path.cwd() / subfolder_name / "overheads-day-90.csv"
print(fp)

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

# create an empty list for overheads record
    overheads=[] 

    # append cash on hand record into the overheads list
    for row in reader:
        #get the "Category", "Overheads" for each record
        #and append to the overheads list
        overheads.append([row[0],float(row[1])])   

print(overheads)