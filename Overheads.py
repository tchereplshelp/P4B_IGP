from pathlib import Path
import csv

# create a file path to the CSV file
fp = Path.cwd() / "overheads-day-90.csv"

# read the CSV file
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    # create an empty list for cash on hand records as dictionaries
    overheads = []

    # append cash on hand records into the cash_on_hand list as dictionaries
    for row in reader:
        overheads.append({row[0], float(row[1])})

print(type(overheads[0]))