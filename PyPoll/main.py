# Dependencies

import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
# print(csvpath)

# Lists or dictionaries?
totalVote = 0
voteReceived = []
# tally = {
    # candNames: counter of votes
# }
# tallyDict = {voteReceived: 0 for voteReceived in voteReceived}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read header row
    csv_header = next(csvreader)

    for row in csvreader: 
        # Counter of total votes
        totalVote += 1

        # Find unique names
        if row[2] not in voteReceived: 
            voteReceived.append(row[2])
        
        # if row[2] == tallyDict

tallyDict = {voteReceived: 0 for voteReceived in voteReceived}
# tally["candNames"] = voteReceived

print(totalVote)
print(voteReceived)
print(tallyDict)