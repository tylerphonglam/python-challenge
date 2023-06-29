#Import module
import os
import csv
#Import address
budgetdata = os.path.join('..','Resources','budget_data.csv')
#Tell python to open them up
with open(budgetdata) as file:
    csvreader = csv.reader(file, delimiter=',') #',' indicate the separation of the file
    next (csvreader) #start with 2nd row because of header
    #in the csv file, loop through the data
    #for every row in the file
    #based on instructions we need, 
    total_months = 0
    total_profit_losses = 0
    # total = new - old
    old_profit_losses = 1088983.0 #start with the last data
    average_change = 0
    changes = [] # a virtutal list with [] bracket
    greatest_increase = ["",(0)]
    greatest_decrease = ["",(0)] 
    #Greatest increase/decrease comes with date => a list of str + int
    for row in csvreader:
        #address profit_losses
        profit_losses = row[1]
        #turn str to int
        profit_losses = int(profit_losses)
        date = row[0] #import to data table a list of date row
        #Part 1. The total number of months, +1 for every line
        total_months += 1
        #Part 2. Net total amount of "Profit/losses"
        total_profit_losses += profit_losses
        #Part 3. Calculate 1 change
        change = profit_losses - old_profit_losses
            #Put all change to a virtual table
        changes.append(change)
        old_profit_losses = profit_losses
        #Part 4. Greatest increase or decrease
        if change >= max(changes):
            greatest_increase = [date,change]
        if change <= min(changes):
            greatest_decrease = [date,change]

    average_change = sum(changes) / len(changes)
#output 
budgetoutput = [
    "Financial Analysis",
    "------------------------",
    f"Total Months: {total_months}",
    f"Total: ${total_profit_losses}",
    f"Average Change: ${average_change:.2f}",
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})",
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
    ]
#to terminal by row
for output in budgetoutput:
    print(output)
#to txt file
output_file = "budget_data_output.txt"
with open(output_file, "w") as file:
    for output in budgetoutput:
        file.write(output + "\n")
