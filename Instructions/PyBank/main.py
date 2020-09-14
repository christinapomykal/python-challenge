import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    totalMonths=0

    #totalMonths=len(list(csvreader))

    #print(totalMonths, " = total number of months in dataset")

    # Read each row of data after the header

    for row in csvreader:
        #print(row)
        print(row[1])
        totalMonths=totalMonths+1

    print(totalMonths)