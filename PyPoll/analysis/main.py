#Import module
import os
import csv
#Path file
election_data = os.path.join('..','Resources','election_data.csv')
with open(election_data) as file:
    election_csv = csv.reader(file, delimiter=',')
    next (election_csv)
    #set intial data
    total_votes = 0
    candidates = {}
    vote_percentage = {}
    winner = ""
    winner_vote = 0
    polloutput = []
    for row in election_csv:
        #Part 1. Total vote
        total_votes += 1
        #Part 2. List of candidates
        name = row[2]
        if name in candidates:
            candidates[name] += 1
        else:
            candidates[name] = 1
        if candidates[name] > winner_vote:
            winner_vote = candidates[name]
            winner = name
#Part 3 percentage of vote
for name, votes in candidates.items():
    percentage = (votes/total_votes)*100
    vote_percentage[name]=percentage
#output
polloutput=[
    "Election Results",
    "-----------------------",
    f"Total Votes: {total_votes}",
    "-----------------------",
]
for name, votes in candidates.items():
    percentage = vote_percentage[name]
    polloutput.append(f"{name}: {percentage:.3f}% ({votes})")
polloutput.extend([
    "-----------------------",
    f"Winner: {winner}",
    "-----------------------",
])
#print by rows
for result in polloutput:
    #to terminal
    print(result)
#To txt file
output = "Poll_data_output.txt"
with open(output, "w") as file:
    for result in polloutput:
        file.write(result + "\n")





