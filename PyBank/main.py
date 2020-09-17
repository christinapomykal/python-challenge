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
    
    # is the same as: netTotal = netTotal + int(profitLoss[i])
    netTotal += int(profitLoss[i])
    # print(str(netTotal))

    if i > 0:
        # conditional to start at index 1, calculate delta from month to month
        currentDelta = int(profitLoss[i]) - int(profitLoss[i - 1])
        
        # adding values to deltaList
        deltaList.append(currentDelta) 
        # print("Current Delta: " + str(currentDelta))
        
        # compare the deltas and keep the larger for profits
        if currentDelta > biggestDelta:
            biggestDelta = currentDelta
            biggestDeltaDate = date[i]
        
        # compare the deltas and keep the smaller for losses
        if currentDelta < biggestLoss:
            biggestLoss = currentDelta
            biggestLossDate = date[i]

avgChange = sum(deltaList) / len(deltaList)

print("Financial Analysis")
print("--------------------------------")
print("Total Months: " + str(len(date)))
print("Grand Total: $" + str(netTotal))
print("Average Change: $" + str(round(avgChange, 2)))
print("Greatest Increase in Profits: " + str(biggestDeltaDate) + " ($" + str(biggestDelta) + ")")
print("Greatest Decrease in Profits: " + str(biggestLossDate) + " ($" + str(biggestLoss) + ")")

output_path = os.path.join("Analysis", "pyBankAnalysis.txt")
# print(output_path)

with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("--------------------------------\n")
    txtfile.write("Total Months: " + str(len(date)) + "\n")
    txtfile.write("Grand Total: $" + str(netTotal) + "\n")
    txtfile.write("Average Change: $" + str(round(avgChange, 2)) + "\n")
    txtfile.write("Greatest Increase in Profits: " + str(biggestDeltaDate) + " ($" + str(biggestDelta) + ")\n")
    txtfile.write("Greatest Decrease in Profits: " + str(biggestLossDate) + " ($" + str(biggestLoss) + ")\n")
