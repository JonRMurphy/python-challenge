# PyBank

# Importing necessary modules
import os

import csv

# Printing the header for the results
print('Financial Analysis')
print('---------------------------------------------------------')

# Creating path to csv file and opening the file
csvpath = os.path.join('PyBank/Resources/budget_data.csv')

with open(csvpath) as csvfile:

    # Reading csv file and skipping the header of the file
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    # Setting lists and variables to hold necessary information
    totalMonths = []
    total = []
    dates = []
    changeList = []

    totalChange = 0
    lastProfit = 0

    for row in csvreader:
        
        # Getting number of months
        totalMonths.append(row[0])

        # Adding up total profits
        total.append(row[1])

        # Storing dates to use later
        dates.append(row[0])

        # Calculating Monthly Changes and storing in list
        currentProfit = int(row[1])       
        changes = currentProfit - lastProfit
        changeList.append(changes)

        # Calculating Average Change
        totalChange += changes
        lastProfit = currentProfit
        avgChange = totalChange / len(totalMonths)


        # Grabbing values for Greateast Increase in Profit and Greatest Decrease in Profit
        gip = max(changeList)
        gdp = min(changeList)
        gipDate = dates[changeList.index(gip)]
        gdpDate = dates[changeList.index(gdp)]

    # Converting total list values from strings to integers
    totalSum = [int(t) for t in total] 
    
    # Printing Results
    print('Total Months: ' + str(len(totalMonths)))
    print('Total: $' + str(sum(totalSum)))
    print('Average Change: $' + str(int(avgChange)))
    print('Greatest Increase in Profits: ' + str(gipDate) + ' ($' + str(gip) + ')')
    print('Greatest Decrease in Profits: ' + str(gdpDate) + ' ($' + str(gdp) + ')')
    print('---------------------------------------------------------')

# Writing results into analysis folder
with open('PyBank/analysis/PyBank Results', 'w') as text:
    text.write('Financial Analysis' + '\n'\
               '---------------------------------------------------------\n'\
               'Total Months: ' + str(len(totalMonths)) + '\n'\
               'Total: $' + str(sum(totalSum)) + '\n'\
               'Average Change: $' + str(int(avgChange)) + '\n'\
               'Greatest Increase in Profits: ' + str(gipDate) + ' ($' + str(gip) + ')\n'\
               'Greatest Decrease in Profits: ' + str(gdpDate) + ' ($' + str(gdp) + ')\n'\
               '---------------------------------------------------------')