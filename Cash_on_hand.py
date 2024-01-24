from pathlib import Path
import csv

# create a file path to csv file in the subfolder named "csv_reports"
subfolder_name = "csv_reports"
fp = Path.cwd() / subfolder_name / "cash-on-hand-sgd.csv"
print(fp)

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

# create an empty list for cash_on_hand record
    cash_on_hand_sgd=[] 

    # append cash on hand record into the cash_on_hand_sgd list
    for row in reader:
        #get the "Day","Cash On Hand" for each record
        #and append to the cash_on_hand_sgd list
        cash_on_hand_sgd.append([row[0],row[1]])   

print(cash_on_hand_sgd)