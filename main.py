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

# PyPoll

# Printing header for results
print('Election Results')
print('---------------------------------------')

# Creating the path and opening the file
election_csv = os.path.join('PyPoll/Resources/election_data.csv')
with open(election_csv) as election:

    # Reading the csv file and skipping the header
    election_reader = csv.reader(election, delimiter=',')
    election_header = next(election)

    # Setting lists to store information of votes for each contestant, total votes, and the winner
    totalVotes = []
    charles = []
    diana = []
    raymon =[]
    winner = []
    
    # Adding vote results to the lists
    for row in election:
        totalVotes.append(row[0])
        if 'Charles' in row[0:100]:
                charles.append(1)
        elif 'Diana' in row[0:100]:
                diana.append(1)
        elif 'Raymon' in row[0:100]:
                raymon.append(1)
       
    # Finding the winner
    if (len(charles)) > (len(diana)) and (len(charles)) > (len(raymon)):
         winner.append('Charles Casper Stockham')
    elif (len(diana) > len(charles)) and (len(diana) > (len(raymon))):
        winner.append('Diana DeGette')
    elif (len(raymon) > (len(charles))) and (len(raymon) > (len(diana))):
        winner.append('Raymon Anthony Doane')
    else:
        winner.append('No Winner')
    
    # Printing Results
    print('Total Votes: ' + str(len(totalVotes)))
    
    print('-----------------------------------')
    
    print('Charles Casper Stockham: ' + (str(round(len(charles) / len(totalVotes)*100, 3))) + '%(' + str(len(charles)) + ')')
    print('Diana DeGette: ' + (str(round(len(diana) / len(totalVotes)*100, 3))) + '%(' + str(len(diana)) + ')')
    print('Raymon Anthony Doane: ' + (str(round(len(raymon) / len(totalVotes)*100, 3))) + '%(' + str(len(raymon)) + ')')
    
    print('-----------------------------------')
    
    print('Winner: ' + (str(winner[0])))
   
    print('-----------------------------------')

# # Exporting Text File
with open('PyPoll/analysis/PyPoll Results', 'w') as text:
     
     text.write('Election Results' + '\n'\
    '---------------------------------------\n'\
    'Total Votes: ' + str(len(totalVotes)) + '\n'\
    '-----------------------------------\n'\
    'Charles Casper Stockham: ' + (str(round(len(charles) / len(totalVotes)*100, 3))) + '%(' + str(len(charles)) + ')\n'\
    'Diana DeGette: ' + (str(round(len(diana) / len(totalVotes)*100, 3))) + '%(' + str(len(diana)) + ')\n'\
    'Raymon Anthony Doane: ' + (str(round(len(raymon) / len(totalVotes)*100, 3))) + '%(' + str(len(raymon)) + ')\n'\
    '-----------------------------------\n'\
    'Winner: '+ (str(winner[0])) + '\n'\
    '-----------------------------------')