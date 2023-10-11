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

        avgChange = round(sum(int(total)) / len(int(total)) * 100, 2)
        gip = max(total)
        gdp = min(total)

print(f'Total Months: ' + str(len(totalMonths)),\
'Total: $' + str(sum(total)),\
'Average Change: $' + str(avgChange),\
'Greatest Increase in Profits: ' + str(gip),\
'Greatest Decrease in Profits: ' + str(gdp))

# PyPoll

# print('Election Results')
# print('---------------------------------------')

# # Creating the path and opening the file
# election_csv = os.path.join('PyPoll/Resources/election_data.csv')
# with open(election_csv) as election:

#     # Reading the csv file and skipping the header
#     election_reader = csv.reader(election, delimiter=',')
#     election_header = next(election)

#     # Setting lists to store information of votes for each contestant, total votes, and the winner
#     totalVotes = []
#     charles = []
#     diana = []
#     raymon =[]
#     winner = []
    
#     # Adding vote results to the lists
#     for row in election:
#         totalVotes.append(row[0])
#         if 'Charles' in row[0:100]:
#                 charles.append(1)
#         elif 'Diana' in row[0:100]:
#                 diana.append(1)
#         elif 'Raymon' in row[0:100]:
#                 raymon.append(1)
       
#     # Finding the winner
    
#     if (len(charles)) > (len(diana)) and (len(charles)) > (len(raymon)):
#          winner.append('Charles Casper Stockham')
#     elif (len(diana) > len(charles)) and (len(diana) > (len(raymon))):
#         winner.append('Diana DeGette')
#     elif (len(raymon) > (len(charles))) and (len(raymon) > (len(diana))):
#         winner.append('Raymon Anthony Doane')
#     else:
#         winner.append('No Winner')
    
#     # Printing Results
#     print('Total Votes: ' + str(len(totalVotes)))
#     print('-----------------------------------')
#     print('Charles Casper Stockham: ' + (str(round(len(charles) / len(totalVotes)*100, 3))) + '%(' + str(len(charles)) + ')')
#     print('Diana DeGette: ' + (str(round(len(diana) / len(totalVotes)*100, 3))) + '%(' + str(len(diana)) + ')')
#     print('Raymon Anthony Doane: ' + (str(round(len(raymon) / len(totalVotes)*100, 3))) + '%(' + str(len(raymon)) + ')')
#     print('-----------------------------------')
#     print('Winner: ' + (str(winner[0])))
#     print('-----------------------------------')