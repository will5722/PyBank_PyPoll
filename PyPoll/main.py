import os
import csv

#Path to election data
election_csv = os.path.join('Resources', 'election_data.csv')
#Open and read data
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

#Set variables/parameters to track, put name of candidate in loop
    TotalVotes = 0
    CandidateList = []
    CandidateVotes = {}


    #Loop through rows, find each candidate, add votes to each
    for row in csvreader:
        TotalVotes += 1
        Name = row[2]
        if Name in CandidateList:
            CandidateVotes[Name] += 1
        else:
            CandidateList.append(Name)
            CandidateVotes[Name] = 0
            CandidateVotes[Name] += 1

    #Find percentage of votes for each candidate by adding to dict
    # then find a winner by going through dict/lists
    CandidateVotes['Percent_Khan'] = round(CandidateVotes['Khan'] / TotalVotes * 100, 3)
    CandidateVotes['Percent_Correy'] = round(CandidateVotes['Correy'] / TotalVotes * 100, 3)
    CandidateVotes['Percent_Li'] = round(CandidateVotes['Li'] / TotalVotes * 100, 3)
    CandidateVotes["Percent_O'Tooley"] = round(CandidateVotes["O'Tooley"] / TotalVotes * 100, 3)
    
    #Find winner, need the key associated with the highest amount of votes
    winner = max(CandidateVotes, key=CandidateVotes.get)


    print("Election Results")
    print("----------------------")
    print(f"Total Votes: {TotalVotes}")
    print("----------------------")
    print(f"Khan: {CandidateVotes['Percent_Khan']}% ({CandidateVotes['Khan']})")
    print(f"Correy: {CandidateVotes['Percent_Correy']}% ({CandidateVotes['Correy']})")
    print(f"Li: {CandidateVotes['Percent_Li']}% ({CandidateVotes['Li']})")
    #Apostrophe in name made using f string difficult
    print("O'Tooley: " + str(CandidateVotes["Percent_O'Tooley"]) + "% " + "(" + str(CandidateVotes["O'Tooley"]) + ")")
    print("----------------------")
    print(f"Winner: {winner}")
    print("----------------------")

#Export analysis to .txt file
output_file = os.path.join('Analysis', 'Election_Analysis.txt')
with open(output_file, 'w') as txtfile:
    txtfile.write("Election Results" + "\n")
    txtfile.write("----------------------"  + "\n")
    txtfile.write(f"Total Votes: {TotalVotes}"  + "\n")
    txtfile.write("----------------------" + "\n")
    txtfile.write(f"Khan: {CandidateVotes['Percent_Khan']}% ({CandidateVotes['Khan']})" + "\n")
    txtfile.write(f"Correy: {CandidateVotes['Percent_Correy']}% ({CandidateVotes['Correy']})" + "\n")
    txtfile.write(f"Li: {CandidateVotes['Percent_Li']}% ({CandidateVotes['Li']})" + "\n")
    #Apostrophe in name made using f string difficult
    txtfile.write("O'Tooley: " + str(CandidateVotes["Percent_O'Tooley"]) + "% " + "(" + str(CandidateVotes["O'Tooley"]) + ")" + "\n")
    txtfile.write("----------------------" + "\n")
    txtfile.write(f"Winner: {winner}" + "\n")
    txtfile.write("----------------------" + "\n")
