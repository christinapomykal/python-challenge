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
biggestLoss = 0
biggestLossDate = ""
deltaList = []

for i in range(len(profitLoss)):
    # print(str(i) + "--" + str(profitLoss[i]) + "-- On: " + date[i])
    # is the same as: netTotal += profitLoss[i]
    netTotal = netTotal + int(profitLoss[i])
    # print(str(netTotal))

    if i > 0:
        currentDelta = int(profitLoss[i]) - int(profitLoss[i - 1])
        
        # adding values to deltaList
        deltaList.append(currentDelta) 
        # print("Current Delta: " + str(currentDelta))
        if currentDelta > biggestDelta:
            biggestDelta = currentDelta
            biggestDeltaDate = date[i]


        
        if currentDelta < biggestLoss:
            biggestLoss = currentDelta
            biggestLossDate = date[i]

avgChange = 

print("Grand Total: " + str(netTotal))

print("Biggest Delta Date: " + str(biggestDeltaDate))
print("Biggest Delta: " + str(biggestDelta))
print("Biggest Loss Date: " + str(biggestLossDate))
print("Biggest Loss: " + str(biggestLoss))
    



    

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