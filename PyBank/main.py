import os
import csv

def print_percentages(budget_data):

print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {}")
print(f"Total: {}")
print(f"Average Change: {}")
print(f"Greatest Increase in Profits: {}")
print(f"Greatest Decrease in Profits: {}")

budget_csv = os.path.join("../Resources", "budget_data.csv")
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    for row in csvreader:
        if(check == row[0]):
            print_percentages(row)
