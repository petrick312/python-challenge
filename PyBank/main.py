#import modules
import os
import csv

#set path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")

#set lists and variables to store data
date = []
total_change = []
total_months = 0
net_total = 0
first_row = 0
next_row = 0
monthly_change = 0

#open and read csv
with open(budget_csv, encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    #loop through csv file
    for row in csv_reader:
        
        #the total number of months included in the dataset
        total_months = total_months + 1
        
        #the net total amount of "Profit/Losses" over the entire period
        net_total = net_total + int(row[1])
    
        #the changes in "Profit/Losses" over the entire period
        first_row = int(row[1])

        if total_months == 1:
            next_row = first_row
        
        else:
            monthly_change = first_row - next_row
            date.append(row[0])
            total_change.append(monthly_change)
            next_row = first_row
    
    #then the average of those changes
    average = round(sum(total_change)/(total_months - 1), 2)

    #the greatest increase in profits (date and amount) over the entire period
    inc_amt = max(total_change)
    inc_date = date[total_change.index(inc_amt)]
                
    #the greatest decrease in profits (date and amount) over the entire period
    dec_amt = (min(total_change))
    dec_date = date[total_change.index(dec_amt)]

#display results
print(f'Financial Analysis\n')
print(f'----------------------------\n')
print(f'Total Months: {total_months}\n')
print(f'Total: ${net_total}\n')
print(f'Average Change: ${average}\n')
print(f'Greatest Increase in Profits: {inc_date} ${inc_amt}\n')
print(f'Greatest Decrease in Profits: {dec_date} ${dec_amt}\n')

#specify the path and file to write to
output_path = os.path.join("analysis", "Financial_Analysis.txt")

#open and write results to text file
with open(output_path,'w', newline='') as text:
    text.write(f'Financial Analysis\n\n')
    text.write(f'----------------------------\n\n')
    text.write(f'Total Months: {total_months}\n\n')
    text.write(f'Total: ${net_total}\n\n')
    text.write(f'Average Change: ${average}\n\n')
    text.write(f'Greatest Increase in Profits: {inc_date} ${inc_amt}\n\n')
    text.write(f'Greatest Decrease in Profits: {dec_date} ${dec_amt}\n\n')
