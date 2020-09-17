# Import os and csv modules

import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
print(csvpath)

# Lists of data or dictionaries? look at class 3_1, activity 08 wrestling
vote = []
candidate = []

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read header row first (skip if no header)
    csv_header = next(csvreader)

    for row in csvreader: 
        vote.append(row[0])
        
        