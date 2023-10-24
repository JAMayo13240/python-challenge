import os
import csv
import pandas as pd
csvpath = os.path.join('Resources','election_data.csv')

results_path = os.path.join("analysis","results.txt")

total = 0
ccs = 0
dd = 0
rad = 0


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    for row in csvreader:
        #Tallying all votes
        total +=1
        #Creating a conditional to tally for respective candidate
        if row[2] == 'Charles Casper Stockham':
            ccs +=1
        elif row[2] == 'Diana DeGette':
            dd +=1
        else:
            rad +=1
    
    percent_of_ccs=(ccs/total)*100
    percent_of_dd=(dd/total)*100
    percent_of_rad=(rad/total)*100
with open(results_path, 'w') as file:
    file.write(f'Total Votes: {total}\n')
    file.write('---------------------------------------------------------------\n')
    file.write(f'Charles Casper Stockham: {ccs} votes ({percent_of_ccs}%)\n')
    file.write(f'Diana DeGette: {dd} votes ({percent_of_dd}%)\n')
    file.write(f'Raymon Anthony Doane: {rad} votes ({percent_of_rad}%)\n')
    file.write('---------------------------------------------------------------\n')    
    file.write('Winner is Diana DeGette')