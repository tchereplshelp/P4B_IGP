from Cash_on_hand import *
from Overheads import *
from Profit_Loss import *
from pathlib import Path

ordinal_suffix = {1: "ST", 2: "ND", 3: "RD"}

# Define the path for the summary report text file
summary_report_path = Path.cwd() / "summary_report.txt"

# Open the summary report file in write mode
with summary_report_path.open(mode="w", encoding="UTF-8") as summary_report:
    
    # Check if there is an increasing trend
    if increasing:
        # Write the highest overhead category and amount to the summary report
        summary_report.write(f"[HIGHEST OVERHEAD]{highest_overhead_category.upper()}: {highest_overhead_amount}%\n")
        
        # Write the trend information for Cash-on-Hand
        summary_report.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        for i, cash_data in enumerate(analyze_top_deficitorsurplus_cash(cash_on_hand_diff), start=1):
            summary_report.write(f"[HIGHEST CASH SURPLUS] DAY: {cash_data[1]}, AMOUNT: SGD {cash_data[2]}")
        
        # Write the trend information for Net Profit
        summary_report.write("[NET PROFIT SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        for i, nets_data in enumerate(analyze_top_deficitorsurplus_nets(net_profit_diff), start=1):
            summary_report.write(f"[HIGHEST NET PROFIT SURPLUS] DAY: {nets_data[1]}, AMOUNT: SGD {nets_data[2]}")
    
    # Check if there is a decreasing trend
    elif decreasing:
        # Write the highest overhead category and amount to the summary report
        summary_report.write(f"[HIGHEST OVERHEAD]{highest_overhead_category.upper()}: {highest_overhead_amount}%\n")
        
        # Write the trend information for Cash-on-Hand
        summary_report.write("[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY")
        for i, cash_data in enumerate(analyze_top_deficitorsurplus_cash(cash_on_hand_diff), start=1):
            summary_report.write(f"[HIGHEST CASH DEFICIT] DAY: {cash_data[1]}, AMOUNT: SGD {cash_data[2]}")
        
        # Write the trend information for Net Profit
        summary_report.write("[NET PROFIT DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY")
        for i, nets_data in enumerate(analyze_top_deficitorsurplus_nets(net_profit_diff), start=1):
            summary_report.write(f"[HIGHEST NET PROFIT DEFICIT] DAY: {nets_data[1]}, AMOUNT: SGD {nets_data[2]}")
    
    # Check if there is a fluctuating trend
    elif fluctuating:
        # Write the highest overhead category and amount to the summary report
        summary_report.write(f"[HIGHEST OVERHEAD]{highest_overhead_category.upper()}: {highest_overhead_amount}%\n")

        # Write days with deficit in Cash-on-Hand
        summary_report.write("Days with deficit in Cash-on-Hand:\n".upper())
        for day_cash, deficit_amount_cash in analyze_cash_on_hand(cash_on_hand_diff):
            summary_report.write(f"[CASH DEFICIT] DAY {day_cash}, AMOUNT: SGD {deficit_amount_cash}\n")

        # Write top 3 highest deficit amounts in Cash-on-Hand
        summary_report.write("Top 3 highest deficit amounts in Cash-on-Hand:\n".upper())
        for i, cash_data in enumerate(analyze_top_deficitorsurplus_cash(cash_on_hand_diff), start=1):
            suffix = ordinal_suffix.get(i, "th")  # Correctly determine the suffix
            summary_report.write(f"[{i}{suffix} HIGHEST CASH DEFICIT] DAY: {cash_data[1]}, AMOUNT: SGD{cash_data[2]}\n")

        # Write days with deficit in Net Profit
        summary_report.write("Days with deficit in Net Profit:\n".upper())
        for day_net, deficit_amount_net in analyze_net_profit(net_profit_diff):
            summary_report.write(f"[NET PROFIT DEFICIT] DAY: {day_net}, AMOUNT: SGD{deficit_amount_net}\n")

        # Write top 3 highest deficit amounts in Net Profit
        summary_report.write("Top 3 highest deficit amounts in Net Profit:\n".upper())
        for i, nets_data in enumerate(analyze_top_deficitorsurplus_nets(net_profit_diff), start=1):
            suffix = ordinal_suffix.get(i, "th")  # Correctly determine the suffix
            summary_report.write(f"[{i}{suffix} HIGHEST NET PROFIT DEFICIT] DAY: {nets_data[1]}, AMOUNT: SGD{nets_data[2]}\n")
