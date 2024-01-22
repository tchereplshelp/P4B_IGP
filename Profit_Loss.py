


from pathlib import Path
import csv
# create a file path to csv file.
fp = Path.cwd()/"profit-and-loss-sgd.csv"
print(fp)

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list for delivery record
    profit_and_loss_sgd=[] 

    # append cash on hand record into the cash_on_hand_sgd list
    for row in reader:
        #get the driver id, sales, distance, and event type for each record
        #and append to the deliveryRecords list
        profit_and_loss_sgd.append([row[0],row[1],row[3],row[4]])   

print(profit_and_loss_sgd)