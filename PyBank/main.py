import os
import csv
import pandas as pd
csvpath = os.path.join('Resources','budget_data.csv')

results_path = os.path.join("analysis","results.txt")

months = 0
total = 0
greatest_increase = 0
greatest_decrease = 0
changes = 0
previous_change = 0

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    
    for row in csvreader:
        
        #Totalling the months
        months +=1
        #Totalling all financial changes
        total += float(row[1])
        
        #Average Changes across the entire period
        current_change=float(row[1])-previous_change
        previous_change=float(row[1])
        changes += current_change
        if current_change>previous_change:
            greatest_increase=current_change
            date_increase = row[0]
        if current_change<previous_change:
            greatest_decrease=current_change
            date_decrease = row[0]

    final_average_change = changes/months   
  
with open(results_path, 'w') as file:
    file.write(f'Total Months: {months}\n')
    file.write('--------------------------------------\n')
    file.write(f'$ {total}\n')
    file.write(f'$ {final_average_change}\n')
    file.write(f'Greatest Increase Month: {date_increase} ({greatest_increase})\n')
    file.write(f'Greatest Decrease Month: {date_decrease} ({greatest_decrease})')