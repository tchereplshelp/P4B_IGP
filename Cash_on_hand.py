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

def calc_diff_in_cash_on_hand(cash_on_hand_data):
    """
    Calculate the difference in Cash-on-Hand between consecutive days.

    Parameters:
    - cash_on_hand_data: List of lists containing cash on hand data for each day.

    Returns:
    - List of tuples containing day and the difference in Cash-on-Hand.
    """
    cash_on_hand_diff = []

    for i in range(1, len(cash_on_hand_data)):
        # Extract relevant information for the current and previous days
        current_day, current_cash_on_hand = int(cash_on_hand_data[i][0]), float(cash_on_hand_data[i][1])
        previous_day, previous_cash_on_hand = int(cash_on_hand_data[i - 1][0]), float(cash_on_hand_data[i - 1][1])

        # Calculate the difference in Cash-on-Hand
        diff_in_cash_on_hand = current_cash_on_hand - previous_cash_on_hand

        # Append the result to the cash_on_hand_diff list
        cash_on_hand_diff.append((current_day, diff_in_cash_on_hand))

    return cash_on_hand_diff

def analyze_cash_on_hand(cash_on_hand_diff):
    """
    Analyze the Cash-on-Hand trends and identify highest increments, decrements, and deficits.

    Parameters:
    - cash_on_hand_diff: List of tuples containing day and the difference in Cash-on-Hand.
    """


    deficit_days = [(day, diff) for day, diff in cash_on_hand_diff if diff < 0]

    if deficit_days:
        top_deficits = sorted(deficit_days, key=get_second_element)[:3]
        print("Days with deficit in Cash-on-Hand:")
        for day, deficit_amount in deficit_days:
            print(f"Day {day}: {deficit_amount}")

        print("\nTop 3 highest deficit amounts in Cash-on-Hand:")
        for day, deficit_amount in top_deficits:
            print(f"Day {day}: {deficit_amount}")

def get_second_element(item):
    return item[1]

# Calculate the difference in Cash-on-Hand
cash_on_hand_diff = calc_diff_in_cash_on_hand(cash_on_hand_sgd)

# Analyze Cash-on-Hand trends
analyze_cash_on_hand(cash_on_hand_diff)
