from pathlib import Path
import csv

# Create a file path to the CSV file in the subfolder named "csv_reports"
subfolder_name = "csv_reports"
fp = Path.cwd() / subfolder_name / "cash-on-hand-sgd.csv"
print(fp)

# Read the CSV file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    # Create an empty list for cash_on_hand record
    cash_on_hand_data = []

    # Append cash on hand record into the cash_on_hand_sgd list
    for row in reader:
        # Get the "Day", "Cash On Hand" for each record
        # and append to the cash_on_hand_data list
        cash_on_hand_data.append([row[0], row[1]])

def calc_diff_in_cash_on_hand(cash_on_hand_data):
    """
    Calculate the difference in Cash-on-Hand between consecutive days.

    Parameters:
    - cash_on_hand_data: List of lists containing cash on hand data for each day.

    Returns:
    - List of tuples containing day and the difference in Cash-on-Hand.
    """
    cash_on_hand_diff = []

    for day in range(1, len(cash_on_hand_data)):
        # Extract relevant information for the current and previous days
        current_day, current_cash_on_hand = int(cash_on_hand_data[day][0]), float(cash_on_hand_data[day][1])
        previous_day, previous_cash_on_hand = int(cash_on_hand_data[day - 1][0]), float(cash_on_hand_data[day - 1][1])

        # Calculate the difference in Cash-on-Hand
        diff_in_cash_on_hand = current_cash_on_hand - previous_cash_on_hand

        # Append the result to the cash_on_hand_diff list
        cash_on_hand_diff.append((current_day, diff_in_cash_on_hand))

    return cash_on_hand_diff
cash_on_hand_diff = calc_diff_in_cash_on_hand(cash_on_hand_data)

# Check the trend of cash on hand
increasing = all(diff >= 0 for day, diff in cash_on_hand_diff)
decreasing = all(diff <= 0 for day, diff in cash_on_hand_diff)
fluctuating = not increasing and not decreasing

def analyze_cash_on_hand(cash_on_hand_diff):
    """
    Analyze the Cash-on-Hand trends and identify days with deficits.

    Parameters:
    - cash_on_hand_diff: List of tuples containing day and the difference in Cash-on-Hand.

    Returns:
    - List of tuples containing day and deficit amount for days with deficits.
    """
    if increasing:
        result_cash = [(day, diff) for day, diff in cash_on_hand_diff if diff > 0]
        return result_cash
    elif decreasing:
        result_cash = [(day, diff) for day, diff in cash_on_hand_diff if diff < 0]
        return result_cash
    elif fluctuating:
        result_cash = [(day, diff) for day, diff in cash_on_hand_diff if diff < 0]
        return result_cash

def analyze_top_deficitorsurplus_cash(result_cash):
    """
    Identify the top 3 highest deficit amounts in Cash-on-Hand.

    Parameters:
    - deficit_days_cash: List of tuples containing day and deficit amount for days with deficits.

    Returns:
    - List of tuples containing position, day, and deficit amount for the top 3 deficits.
    """
    if increasing or decreasing:
        top_analysis_cash = sorted(result_cash, key=get_second_element)[:1]
        #return top surplus or defecit
    elif fluctuating:
        top_analysis_cash = sorted(result_cash, key=get_second_element)[:3]
    # The key parameter is an optional argument that specifies a function of one
    # argument that is used to extract a comparison key from each element in the iterable being sorted.
    # The get_second_element function is a helper function that takes a tuple item as a parameter.
    # It returns the second element of the tuple (item[1]).
    # This function is used as the key function in the sorted call to sort tuples
    # based on their second element (deficit amounts in Cash-on-Hand) in ascending order.
    # This helps in identifying the top 3 highest deficit amounts in Cash-on-Hand.
    cash_result = []
    for i, (days_cash, analysis_amount_cash) in enumerate(top_analysis_cash, start=1):
        cash_result.append((i, days_cash, analysis_amount_cash))
    return cash_result

def get_second_element(item):
    """
    Helper function to get the second element of a tuple.

    Parameters:
    - item: A tuple.

    Returns:
    - The second element of the tuple.
    """
    return item[1]

