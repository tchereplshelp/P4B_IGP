from pathlib import Path
import csv
# create a file path to csv file.
fp = Path.cwd()/"cash-on-hand-sgd.csv"
print(fp)

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list for delivery record
    cash_on_hand_sgd=[] 

    # append cash on hand record into the cash_on_hand_sgd list
    for row in reader:
        #get the driver id, sales, distance, and event type for each record
        #and append to the deliveryRecords list
        cash_on_hand_sgd.append([row[0],row[1],row[2],row[3]])   








# Write the calculated info to a Summary_report.txt file.
from pathlib import Path

# File path for the main solution file 
filepath = Path.cwd()/'summary_report.txt'
with open (filepath, "w") as file:
    file.write("[HIGHEST OVERHEAD]:\n")
    file.write("[CASH SURPLUS]:\n")
    file.write("[HIGHEST CASH SURPLUS]:\n")
    file.write("[NET PROFIT SURPLUS]:\n")
    file.write("[HIGHEST NET PROFIT SURPLUS]:\n")
