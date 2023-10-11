# PyBank

import os

import csv


print('Financial Analysis')
print('-------------------------------------')
# Creating path to csv file
csvpath = os.path.join('PyBank/Resources/budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    # Outcomes for final analysis: Total Months, Total, Average Change, Greatest Increase in Profits, Greatest Decrease in Profits
    totalMonths = []
    total = []
    avgChange = 0

    # For loop to find data
    for row in csvreader:

        totalMonths.append(row[0])

        total.append(row[1])

        gip = max(total)
        gdp = min(total)
    avgChange = round

print(f'Total Months: ' + str(len(totalMonths)),\
'Total: $' + str(sum(total)),\
'Average Change: $' + str(avgChange),\
'Greatest Increase in Profits: ' + str(gip),\
'Greatest Decrease in Profits: ' + str(gdp))

# Exporting Text File
with open('PyBank.py', 'w') as f:
     f.write('PyBankResults')