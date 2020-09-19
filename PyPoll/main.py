# Dependencies

import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
# print(csvpath)

# Counter for total votes
totalVote = 0
# holder for tally dictionary = {uniqueCandName: candsTotalVotes}
tally = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read header row
    csv_header = next(csvreader)

    for row in csvreader: 
        # Counter of total votes
        totalVote += 1

        # Find unique names
        if row[2] not in tally.keys(): 
            # build key with uniqueCandName and add key:value pair to dict with value of 1 vote
            tally[row[2]] = 1
        else:
            # add value 1 vote if uniqueCandName already a key in tally dict
            tally[row[2]] += 1 

# Variables and lists for election results            
winnerVote = 0
winnerName = ""
voter_outputs = []

# After for loop, tally dict now filled with unique keys (uniqueCandName) with the associated value (candsTotalVotes)
for uniqueCandName in tally: 
    
    percentCand = (tally[uniqueCandName] / totalVote * 100)
    voter_output = f"{uniqueCandName}: {percentCand:.3f}% ({tally[uniqueCandName]})"
    voter_outputs.append(voter_output)

    if tally[uniqueCandName] > winnerVote: 
        winnerVote = tally[uniqueCandName]
        winnerName = uniqueCandName

print("Election Results")
print("--------------------")
print(f"Total Votes: {totalVote}")
print("--------------------")    
print(voter_outputs)
print("--------------------")
print(f"Winner: {winnerName}")
print("--------------------")

output_path = os.path.join("Analysis", "pyPollAnalysis.txt")

with open(output_path, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("--------------------\n")
    txtfile.write(f"Total Votes: {totalVote}\n")
    txtfile.write("--------------------\n")
    txtfile.write(f"{voter_outputs}\n")
    txtfile.write("--------------------\n")
    txtfile.write(f"Winner: {winnerName}\n")
    txtfile.write("--------------------\n")
