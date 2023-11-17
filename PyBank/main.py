import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")

total_net = 0
total_months = 0
change_list = []
greatest_increase_change = 0
greatest_decrease_change = 0
greatest_decrease_change_month = ""


with open(budget_csv, encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        
        date = row[0]
        profit_loss = int(row[1])
        total_net = total_net + profit_loss
        total_months = total_months + 1
        if(total_months > 1):
            net_change = profit_loss - previous_profit_loss
            change_list.append(net_change)

            if(net_change > greatest_increase_change):
                greatest_increase_change = net_change
                greatest_increase_change_date = date

            if(net_change < greatest_decrease_change):
                greatest_decrease_change = net_change
                greatest_decrease_change_month = date 

        previous_profit_loss = profit_loss

    average_change = sum(change_list) / len(change_list)

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Net: {total_net}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_change_date} (${greatest_increase_change})")
    print(f"Greatest Decrease in Profits: {greatest_increase_change_date} (${greatest_decrease_change})")

output_path = os.path.join("Analysis", "Analysis.txt")

with open(output_path, 'w') as txtfile:

    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total Net: {total_net}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_change_date} (${greatest_increase_change})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_increase_change_date} (${greatest_decrease_change})\n")