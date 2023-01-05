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
    VoteCount = {}
    VotePercentage = []
    Candidate_Votes = {}
    VoteCountList = []
    results = ""
    combined_results = ""

    # Iterate through the rows in the CSV
    for row in csv_reader:
        Count +=1
        Candidates = row[2]
        if Candidates not in Candidates_No_Dupes:
            Candidates_No_Dupes.append(row[2])
        try: 
            VoteCount[Candidates] +=1
        except:
            VoteCount[Candidates] = 1
        
    for name in VoteCount:
        VotePercentage.append(VoteCount[name] / Count)
        VoteCountList.append(VoteCount[name])

    FormattedVotePercentage = []
    for i in VotePercentage:
        FormattedVotePercentage.append(str(round(i*100, 3)) + "%")

    #Populate a dictionary with results
    Candidate_Votes = {
        "Name" : Candidates_No_Dupes,
        "Vote Count": VoteCountList,
        "Vote Percentage": FormattedVotePercentage
    }

#Output to terminal
print("Election Results")   
print("-------------------------------")
print("Total Votes: ", Count)
print("-------------------------------")
for i in range(0, len(Candidates_No_Dupes)):
    results = f'{Candidate_Votes["Name"][i]}: {Candidate_Votes["Vote Percentage"][i]} ({Candidate_Votes["Vote Count"][i]})'
    combined_results += results + "\n"
print(combined_results)
print("-------------------------------")
for i in range(0, len(Candidates_No_Dupes)):
    if VoteCountList[i] == max(VoteCountList):
        winner = f'{"Winner:", Candidates_No_Dupes[i]}'
        print(winner)
print("-------------------------------")

# Output to text file.
output_file = (f"Election Results\n"   
    f"-------------------------------\n"
    f"Total Votes: {Count}\n"
    f"-------------------------------\n"
    f"{combined_results}\n"
    f"-------------------------------\n"
    f"{winner}\n"
    f"-------------------------------\n")

with open("Output.txt", "w") as f:
    f.write(output_file)
    f.write("\n")    