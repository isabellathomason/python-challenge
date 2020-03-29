
import os
import csv

#loading data files
file_location = "Resources/election_data.csv"

#assigning variables and assigning to start at 0
votes = 0
Khan = 0
Correy = 0
Li = 0
Otooley = 0

#read cvs.reader(election_data)
with open(file_location, "r") as election_data:
    reader = csv.reader(election_data, delimiter=",")

#skip the header
    csvheader = next(reader)

#Create loop through data to find 
    for row in reader:
        votes = votes + 1

        if (row[2] == "Khan"):
            Khan = Khan + 1
        elif (row[2] == "Correy"):
            Correy = Correy +1
        elif (row[2] == "Li"):
            Li = Li + 1
        elif (row[2] == "O'Tooley"):
            Otooley = Otooley + 1

#vote count percent

    percent_Khan = Khan / votes
    percent_Correy = Correy / votes
    percent_Li = Li / votes
    percent_Otooley = Otooley / votes
    
    
winner = max(Khan, Correy, Li, Otooley)

if winner == Khan:
    election_winner = "Khan"
elif winner == Correy:
    election_winner = "Correy"
elif winner == Li:
    election_winner = "Li"
elif winner == Otooley:
    election_winner = "O'Tooley"

        
    #print output
output = (
    f"Election Results\n"
    f"-----------------------------\n"
    f"Total Votes: {votes}\n"
    f"-----------------------------\n"
    f"Khan: {percent_Khan:.3%} (){Khan}\n"
    f"Correy: {percent_Correy:.3%} (){Correy}\n"
    f"Li: {percent_Li:.3%} (){Li}\n"
    f"O'Tooley: {percent_Otooley:.3%} (){Otooley}\n"
    f"-----------------------------\n"
    f"Winner: {election_winner}\n"
    f"-----------------------------\n"
)

print(output)

output_file_location = "PyPoll"

# output
with open(output_file_location, "w") as txtfile:
    txtfile.write(output)