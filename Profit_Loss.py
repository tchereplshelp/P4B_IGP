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
        for day, deficit_amount in top_deficits:
            print(f"Day {day}: {deficit_amount}")


def get_second_element(item):
    return item[1]


# Calculate the difference in net profit
net_profit_diff = calc_diff_in_net_profit(profit_and_loss_sgd)

# Analyze net profit trends
analyze_net_profit(net_profit_diff)


