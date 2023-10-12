# PyPoll

# Importing needed modules
import os
import csv

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