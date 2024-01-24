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

# Find the highest overhead category
def get_overhead_amount(item):
    return item[1]

def find_highest_overhead_category(overheads_data):
    """
    Find the highest overhead category.

    Parameters:
    - overheads_data: List of lists containing overheads data.

    Returns:
    - Tuple containing the highest overhead category and its amount.
    """
    max_overhead_category, max_overhead_amount = max(overheads_data, key=get_overhead_amount)
    return max_overhead_category, max_overhead_amount

# Call the function to find the highest overhead category
highest_overhead_category, highest_overhead_amount = find_highest_overhead_category(overheads)

# Print the result
print(f"The highest overhead category is '{highest_overhead_category}' with an amount of {highest_overhead_amount}.")


from pathlib import Path
import csv

# create a file path to csv file in the subfolder named "csv_reports"
subfolder_name = "csv_reports"
fp = Path.cwd() / subfolder_name / "profit-and-loss-sgd.csv"
print(fp)

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    # create an empty list for profit_and_loss record
    profit_and_loss_sgd = []
    # append profit and loss record into the profit_and_loss_sgd list
    for row in reader:
        # get the "Day","Sales","Trading Profit","Operating Expense","Net Profit" for each record
        # and append to the profit and loss list
        profit_and_loss_sgd.append([row[0], row[1], row[3], row[4]])


def calc_diff_in_net_profit(profit_and_loss_data):
    """
    Calculate the difference in net profit between consecutive days.

    Parameters:
    - profit_and_loss_data: List of lists containing profit and loss data for each day.

    Returns:
    - List of tuples containing day and the difference in net profit.
    """
    net_profit_diff = []

    for i in range(1, len(profit_and_loss_data)):
        # Extract relevant information for the current and previous days
        current_day, current_net_profit = int(profit_and_loss_data[i][0]), float(profit_and_loss_data[i][3])
        previous_day, previous_net_profit = int(profit_and_loss_data[i - 1][0]), float(profit_and_loss_data[i - 1][3])

        # Calculate the difference in net profit
        diff_in_net_profit = current_net_profit - previous_net_profit

        # Append the result to the net_profit_diff list
        net_profit_diff.append((current_day, diff_in_net_profit))

    return net_profit_diff


def analyze_net_profit(net_profit_diff):
    """
    Analyze the net profit trends and identify highest increments, decrements, and deficits.

    Parameters:
    - net_profit_diff: List of tuples containing day and the difference in net profit.
    """
    deficit_days = [(day, diff) for day, diff in net_profit_diff if diff < 0]

    if deficit_days:
        top_deficits = sorted(deficit_days, key=get_second_element)[:3]
        print("Days with deficit:")
        for day, deficit_amount in deficit_days:
            print(f"Day {day}: {deficit_amount}")

        print("\nTop 3 highest deficit amounts:")
        for days, deficit_amount_top in top_deficits:
            print(f"Day {days}: {deficit_amount_top}")


def get_second_element(item):
    return item[1]


# Calculate the difference in net profit
net_profit_diff = calc_diff_in_net_profit(profit_and_loss_sgd)

# Analyze net profit trends
analyze_net_profit(net_profit_diff)

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
        for days2, deficit_amount_top_cash in top_deficits:
            print(f"Day {days2}: {deficit_amount_top_cash}")

def get_second_element(item):
    return item[1]

# Calculate the difference in Cash-on-Hand
cash_on_hand_diff = calc_diff_in_cash_on_hand(cash_on_hand_sgd)

# Analyze Cash-on-Hand trends
analyze_cash_on_hand(cash_on_hand_diff)


# Assuming highest_overhead_category and highest_overhead_amount are given
# and that you have lists called cash_on_hand_diff and net_profit_diff that
# contain the daily differences for cash on hand and net profit, respectively.

# Find the day with the highest cash deficit
highest_cash_deficit_day, highest_cash_deficit_amount = min(cash_on_hand_diff, key=get_second_element)

# Find the day with the highest net profit deficit
highest_profit_deficit_day, highest_profit_deficit_amount = min(net_profit_diff, key=get_second_element)

# Calculate the highest overhead percentage
highest_overhead_percentage = (highest_overhead_amount / sum([amount for _, amount in overheads])) * 100

# Write the calculated info to a Summary_report.txt file.
summary_report_path = Path.cwd() / 'summary_report.txt'
with open(summary_report_path, "w") as file:
    file.write(f"[HIGHEST OVERHEAD] {highest_overhead_category.upper()}: {highest_overhead_percentage:.2f}%\n")
    file.write("[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\n")
    file.write(f"[HIGHEST CASH DEFICIT] DAY: {highest_cash_deficit_day}, AMOUNT: {highest_cash_deficit_amount}\n")
    file.write("[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY\n")
    file.write(f"[HIGHEST PROFIT DEFICIT] DAY {highest_profit_deficit_day}, AMOUNT: {highest_profit_deficit_amount}\n")

# Print path of the summary report file
print(f"Summary report written to: {summary_report_path}")

