# import necessary modules
import os
import csv

# find file path
file = os.path.join('Resources', 'budget_data.csv')

# create empty tables to add to
profitloss = []
months = []
pnlchange = []

# make file readable 
with open(file) as csvfile:
    filereader = csv.reader(csvfile, delimiter=",")
    next(filereader)
    # add together total P/L
    for row in filereader:
        profitloss.append(int(row[1]))
        months.append(row[0])
# name usable variables
totalPNL = sum(profitloss)
numberofmonths = len(months)
start = int(profitloss[0])
for pnl in profitloss[1:]:
    difference = int(pnl) - int(start)
    pnlchange.append(difference)
    start = int(pnl)
averagechange = round(sum(pnlchange)/len(pnlchange), 2)
maxpnl = max(pnlchange)
minpnl = min(pnlchange)
maxmonthindex = pnlchange.index(maxpnl) + 1
minmonthindex = pnlchange.index(minpnl) + 1
maxmonth = months[maxmonthindex]
minmonth = months[minmonthindex]   
    

print("```text")
print("Financial Analysis")
print("----------------")
print(f"Total months: {numberofmonths}")
print(f"Total Profit/Loss: ${totalPNL}")
print(f"Average Change: ${averagechange}")
print(f"Greatest Increase in Profits: {maxmonth} ${maxpnl}")
print(f"Greatest Decrease in Profits: {minmonth} ${minpnl}")
print("```")

output = open("Analysis\output.csv", "w")
output.write("```text\n")
output.write("Financial Analysis\n")
output.write("----------------\n")
output.write(f"Total months: {numberofmonths}\n")
output.write(f"Total Profit/Loss: ${totalPNL}\n")
output.write(f"Average Change: ${averagechange}\n")
output.write(f"Greatest Increase in Profits: {maxmonth} ${maxpnl}\n")
output.write(f"Greatest Decrease in Profits: {minmonth} ${minpnl}\n")
output.write("```\n")