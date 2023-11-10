#import modules
import os
import csv

#set path to collect data from the Resources folder
election_csv = os.path.join("Resources", "election_data.csv")

#set lists and variables to store data
vote_total = 0
cand_votes = {}
cand_votes_perc = {}

#open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    
    #loop through csv file
    for row in csv_reader:

        #the total number of votes cast
        vote_total = vote_total + 1
        
        #a complete list of candidates who received votes
        #the total number of votes each candidate won
        if row[2] in cand_votes:
            cand_votes[row[2]] += 1
        else:
            cand_votes[row[2]] = 1
            
        #the percentage of votes each candidate won
        for key, value in cand_votes.items():
            cand_votes_perc[key] =round((value/vote_total)* 100 , 3)
        
        #the winner of the election based on popular vote - look for max count of votes and store candidate name
        winner = max(cand_votes, key=cand_votes.get)
    
#display the results
print(f'Election Results\n')
print(f'-------------------------\n')
print(f'Total Votes: {vote_total}\n')
print(f'-------------------------\n')
for key, value in cand_votes.items():
    print(f'{key}: {str(cand_votes_perc[key])}% ({cand_votes[key]})\n')
print(f'-------------------------\n')
print(f'Winner: {winner}\n')
print(f'-------------------------\n')

#specify the path and file to write to
output_path = os.path.join("analysis", "Election_Results.txt")
        
#open and write results to text file
with open(output_path,'w', newline='') as text:
    text.write(f'Election Results\n\n')
    text.write(f'-------------------------\n\n')
    text.write(f'Total Votes: {vote_total}\n\n')
    text.write(f'-------------------------\n\n')
    for key, value in cand_votes.items():
        text.write(f'{key}: {str(cand_votes_perc[key])}% ({cand_votes[key]})\n\n')
    text.write(f'-------------------------\n\n')
    text.write(f'Winner: {winner}\n\n')
    text.write(f'-------------------------\n\n')
