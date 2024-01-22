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
        cash_on_hand_sgd.append([row[0],row[1]])   

print(cash_on_hand_sgd)