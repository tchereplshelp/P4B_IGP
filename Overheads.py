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
    overheads_data = []

    # append overheads record into the overheads list
    for row in reader:
        # get the "Category", "Overheads" for each record
        # and append to the overheads list
        overheads_data.append([row[0], float(row[1])])

# Find the highest overhead category
def get_overhead_amount(item):
    """
    Helper function to get the second element of a tuple.

    Parameters:
    - item: A tuple.

    Returns:
    - The second element of the tuple.
    """
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
    # the key parameter is an optional argument that specifies a function of one
    # argument that is used to extract a comparison key from each element in the iterable being sorted
    #The key=get_overhead_amount parameter indicates that the comparison for finding the maximum should be based on the Overheads amount
    #The get_overhead_amount function is a helper function that takes a tuple item as a parameter.
    #It returns the second element of the tuple (item[1]).
    #This function is used as the key function in the max function call to find the maximum element in the overheads_data list 
    # based on the second element of each tuple (Overheads amount).
    return max_overhead_category, max_overhead_amount

# Call the function to find the highest overhead category
highest_overhead_category, highest_overhead_amount = find_highest_overhead_category(overheads_data)

# Print the result
print(f"[HIGHEST OVERHEAD]{highest_overhead_category.upper()}: {highest_overhead_amount}%")
