import os
import csv

print("Financial Analysis")
print("-----------------------")

def print_months(months_data):
    print(f"Total Months: {months_data}")
    
def print_total(total_data):
    print(f"Total: ${total_data}")
    
#def print_average(average_change):
#    print(f"Average Change: ${average_change}")
    
def print_max(greatest_increase, date_increase):
    print(f"Greatest Increase in Profits: {date_increase} ${greatest_increase}")

def print_min(greatest_decrease, date_decrease):
    print(f"Greatest Decrease in Profits: {date_decrease} $-{greatest_decrease}")

budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    count_of_months = 0
    net_total = 0
    maxIncrease = 0
    maxDecrease = 0
    previousRow = 0
    maxDateIncrease = ""
    minDateDecrease = ""
    averageChange = 0
    for row in csvreader:
        count_of_months += 1
        net_total += int(row[1])
        if maxIncrease < int(row[1]) - previousRow:
            maxIncrease = (int(row[1]) - previousRow)
            maxDateIncrease = row[0]
        if maxDecrease < previousRow - int(row[1]):
            maxDecrease = (previousRow - int(row[1]))
            minDateDecrease = row[0]
#        averageChange += (previousRow - int(row[1]))
        previousRow = int(row[1])
    
    print_months(count_of_months)
    print_total(net_total)
#    print_average (averageChange / (count_of_months - 1))
    print_max(maxIncrease, maxDateIncrease)
    print_min(maxDecrease, minDateDecrease)
    

        

        
