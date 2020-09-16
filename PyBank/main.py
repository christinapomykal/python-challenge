# Import os and csv modules

import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
# print(csvpath)

# Lists to store data
date = []
profitLoss = []

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    # print(csvreader)

    # Read header row
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        
        # Add date
        date.append(row[0])

        # Add profitLoss
        profitLoss.append(row[1])
    
# Done reading csvreader. Data in lists. 

print("Total Months: " + str(len(date)))

# for x in profitLoss:
#     print(x)

netTotal = 0
biggestDelta = 0
biggestDeltaDate = ""
deltaList = []

for i in range(len(profitLoss)):
    print(str(i) + "--" + str(profitLoss[i]) + "-- On: " + date[i])
    netTotal = netTotal + int(profitLoss[i]) # is the same as: netTotal += profitLoss[i]
    print(str(netTotal))

    if i > 0:
        currentDelta = int(profitLoss[i]) - int(profitLoss[i - 1])
        print("Current Delta: " + str(currentDelta))
        if currentDelta > biggestDelta:
            biggestDelta = currentDelta
            biggestDeltaDate = date[i]

            print("Biggest Delta: " + str(biggestDeltaDate))

    

print("Grand Total: " + str(netTotal))

    

    # print(len(list(csvreader)))
    # totalMonths=0

    # totalMonths=len(list(csvreader))
    
    # print(totalMonths)

    #print(totalMonths, " = total number of months in dataset")

    # Read each row of data after the header

    # for row in csvreader:
    #     #print(row)
    #     print(row[1])
    #     totalMonths=totalMonths+1

    # print(totalMonths)