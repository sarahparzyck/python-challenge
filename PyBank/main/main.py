import os
import csv

print("Financial Analysis")
print("-----------------------")

def print_months(months_data):
    print(f"Total Months: {months_data}")
    
def print_total(total_data):
    print(f"Total: ${total_data}")
    
def average():
    avg = print_total / print_months
    return avg
    print(f"Average Change: {average}")
    
def print_max(greatest_increase):
    print(f"Greatest Increase in Profits: {greatest_increase}")
##    print(f"Greatest Decrease in Profits: {}")

budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    count_of_months = 0
    net_total = 0
    maxVal = 0
    for row in csvreader:
        count_of_months += 1
        net_total += int(row[1])
        if maxVal < int(row[1]):
            maxVal = int(row[1])
    print_months(count_of_months)
    print_total(net_total)
    print_max(maxVal)

        

        
