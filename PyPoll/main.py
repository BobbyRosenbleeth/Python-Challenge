# Import packages
import os
import csv

# Import CSV
election_csv = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)

    # Establish the necessary variables
    Count = 0
    Candidates = []
    Candidates_No_Dupes = []
    VoteCount_Stockham = 0
    VoteCount_DeGette = 0
    VoteCount_Doane = 0
    Candidate_Votes = {}
    Candidate_Votes = dict()
    
    # Iterate through the rows in the CSV
    for row in csv_reader:
        Count = Count + 1
        Candidates = row[2]
        if Candidates not in Candidates_No_Dupes:
            Candidates_No_Dupes.append(row[2])
        if row[2] == "Charles Casper Stockham":
            VoteCount_Stockham = VoteCount_Stockham + 1
        if row[2] == "Diana DeGette":
            VoteCount_DeGette = VoteCount_DeGette + 1
        if row[2] == "Raymon Anthony Doane":
            VoteCount_Doane = VoteCount_Doane + 1

    VoteCount = [VoteCount_Stockham, VoteCount_DeGette, VoteCount_Doane]            
    VotePercentage = [VoteCount_Stockham/Count, VoteCount_DeGette/Count, VoteCount_Doane/Count]
    FormattedVotePercentage = []
    for i in VotePercentage:
        FormattedVotePercentage.append(str(round(i*100, 3)) + "%")

    #Populate a dictionary with results
    Candidate_Votes = {
        "Name" : Candidates_No_Dupes,
        "Vote Count": VoteCount,
        "Vote Percentage": FormattedVotePercentage
    }

#Output to terminal
print("Election Results")   
print("-------------------------------")
print("Total Votes: ", Count)
print("-------------------------------")
for i in range(0, len(Candidates_No_Dupes)):
    print(f'{Candidate_Votes["Name"][i]}: {Candidate_Votes["Vote Percentage"][i]} ({Candidate_Votes["Vote Count"][i]})')
print("-------------------------------")
for i in range(0, len(Candidates_No_Dupes)):
    if VoteCount[i] == max(VoteCount):
        print("Winner:", Candidates_No_Dupes[i])
print("-------------------------------")

# Output to text file.
four = []

one = "Election Results"
two = "-------------------------------"
three = "Total Votes: ", Count
for i in range(0, len(Candidates_No_Dupes)):
    four.append((Candidate_Votes["Name"][i], ":", Candidate_Votes["Vote Percentage"][i], "(", Candidate_Votes["Vote Count"][i],"')"))
for i in range(0, len(Candidates_No_Dupes)):
    if VoteCount[i] == max(VoteCount):
        five = "Winner:", Candidates_No_Dupes[i]

lines = [one, two, three, two, four, two, five, two] 
with open("Output.txt", "w") as f:
    for line in range(0, len(lines)):
        f.write(str(lines[line]))
        f.write("\n")