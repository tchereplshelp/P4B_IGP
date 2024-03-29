from pathlib import Path
import csv

# Create a file path to the CSV file in the subfolder named "csv_reports"
subfolder_name = "csv_reports"
fp = Path.cwd() / subfolder_name / "profit-and-loss-sgd.csv"
print(fp)

# Read the CSV file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    # Create an empty list for profit_and_loss records
    profit_and_loss_data = []

    # Append profit and loss records into the profit_and_loss_data list
    for row in reader:
        # Get the "Day","Sales","Trading Profit","Operating Expense","Net Profit" for each record
        # and append to the profit_and_loss_data list as a list
        profit_and_loss_data.append([row[0], row[1], row[3], row[4]])

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

        # Append the result to the net_profit_diff list as a tuple
        net_profit_diff.append((current_day, diff_in_net_profit))

    return net_profit_diff

net_profit_diff = calc_diff_in_net_profit(profit_and_loss_data)
# Check the trend of cash on hand
increasing = all(diff >= 0 for day, diff in net_profit_diff)
decreasing = all(diff <= 0 for day, diff in net_profit_diff)
fluctuating = not increasing and not decreasing

def analyze_net_profit(net_profit_diff):
    """
    Analyze the net profit trends and identify highest increments, decrements, and deficits.

    Parameters:
    - net_profit_diff: List of tuples containing day and the difference in net profit.
    """
    # Create a list of tuples containing days and their corresponding amounts
    if increasing:
        result_net = [(day, diff) for day, diff in net_profit_diff if diff > 0]
        return result_net
    elif decreasing:
        result_net = [(day, diff) for day, diff in net_profit_diff if diff < 0]
        return result_net
    elif fluctuating:
        result_net = [(day, diff) for day, diff in net_profit_diff if diff < 0]
        return result_net

def analyze_top_deficitorsurplus_nets(result_net):
    """
    Identify the top 1 highest deficit amount in net profit.

    Parameters:
    - deficit_days_net: List of tuples containing day and deficit amount for days with deficits.

    Returns:
    - List of tuples containing position, day, and deficit amount for the top deficit.
    """
    if increasing or decreasing:
        top_analysis_net = sorted(result_net, key=get_second_element)[:1]
    # Sort the deficit days based on deficit amounts (using the get_second_element function)
    elif fluctuating:
        top_analysis_net = sorted(result_net, key=get_second_element)[:3]
        #The get_second_element function is a helper function that takes a tuple item as a parameter.
        #It returns the second element of the tuple (item[1]).
        #This function is used as the key function in the sorted call to sort tuples 
        #based on their second element (deficit amounts in profit and loss) in ascending order.
        #This helps in identifying the top 1 highest deficit amount in profit and loss.
    # Create a list of tuples with position, day, and deficit amount for the top deficit
    profit_result = []
    for i, (days_net, day_amount_net) in enumerate(top_analysis_net, start=1):
        profit_result.append((i, days_net, day_amount_net))
    return profit_result

def get_second_element(item):
    """
    Helper function to get the second element of a tuple.

    Parameters:
    - item: A tuple.

    Returns:
    - The second element of the tuple.
    """
    return item[1]


