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
