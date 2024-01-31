from Cash_on_hand import *
from Overheads import *
from Profit_Loss import *
from pathlib import Path

summary_report_path = Path.cwd() / "summary_report.txt"
with summary_report_path.open(mode="w", encoding="UTF-8") as summary_report:
    summary_report.write(f"[HIGHEST OVERHEAD]{highest_overhead_category.upper()}: {highest_overhead_amount}%\n")
    summary_report.write("Days with deficit in Cash-on-Hand:\n")
    for day_cash, deficit_amount_cash in analyze_cash_on_hand(cash_on_hand_diff):
        summary_report.write(f"[CASH DEFICIT] DAY {day_cash}, AMOUNT: SGD {deficit_amount_cash}\n")
    summary_report.write("Top 3 highest deficit amounts in Cash-on-Hand:\n")
    for i, cash_data in enumerate(analyze_top_deficit_cash(cash_on_hand_diff), start=1):
        summary_report.write(f"[{i}{suffix} HIGHEST CASH DEFICIT] DAY: {cash_data[1]}, AMOUNT: SGD{cash_data[2]}\n")
    summary_report.write("Days with deficit (profit and loss):\n")
    for day_net, deficit_amount_net in analyze_net_profit(net_profit_diff):
        summary_report.write(f"[NET PROFIT DEFICIT] DAY: {day_net}, AMOUNT: SGD{deficit_amount_net}\n")
    summary_report.write("Top 3 highest deficit amounts in profit and loss:\n")
    for i, nets_data in enumerate(analyze_top_deficit_nets(net_profit_diff), start=1):
        summary_report.write(f"[{i}{suffix} HIGHEST NET PROFIT DEFICIT] DAY: {nets_data[1]}, AMOUNT: SGD{nets_data[2]}\n")


