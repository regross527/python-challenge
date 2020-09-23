import os
import csv

file = os.path.join('Resources', 'election_data.csv')

# create empty sets to be built from csv file
voterid = []
countylist = []
candidatevotes = []

# make file readable 
with open(file) as csvfile:
    filereader = csv.reader(csvfile, delimiter=",")
    next(filereader)
    # add together total P/L
    for row in filereader:
        voterid.append(int(row[0]))
        countylist.append(row[1])
        candidatevotes.append(row[2])

# define variables that go to output
votecount = len(voterid)
candidates = set(candidatevotes)
# found method to find mode via https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/#:~:text=Make%20use%20of%20Python%20Counter,by%20using%20most_common()%20method.&text=Finding%20most%20frequent%20element%20means,use%20mode%20method%20from%20statistics.
import statistics
from statistics import mode
def winner(candidatevotes):
    return mode(candidatevotes)
winner = winner(candidatevotes)


# output starts here 
print("```text")
print("Election Results")
print("-------------")
print(f"Total Votes: {votecount}")
print("-------------")

# create the .txt file
output = open("Analysis/output.csv", "w")
output.write("```text\n")
output.write("Election Results\n")
output.write("-------------\n")
output.write(f"Total Votes: {votecount}\n")
output.write("-------------\n")

# create iterating list of candidates
for name in candidates:
    numberofvotes = candidatevotes.count(name)
    shareofvotes = round(numberofvotes/votecount * 100, 2)
    print(f"{name}: {shareofvotes}% ({numberofvotes})")
    output.write(f"{name}: {shareofvotes}% ({numberofvotes})\n")
print("-------------")
print(f"Winner: {winner}")
print("-------------")
print("```")

output.write("-------------\n")
output.write(f"Winner: {winner}\n")
output.write("-------------\n")
output.write("```\n")