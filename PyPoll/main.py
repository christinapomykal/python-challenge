# Dependencies

import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
# print(csvpath)

# Lists or dictionaries?
totalVote = 0
uniqueCandName = []
# tally is a dict = {uniqueCandName: candsTotalVotes}
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
            
# After for loop, tally dict now filled with unique keys (uniqueCandName) with the associated value (candsTotalVotes)
print(tally)

# Now loop through the dict, and do the math per key:value in dict
# find % by pull value from the dict for that key / totalVote
# Winner is comparing all the values with the key
