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
    

    print(f"Khan: {CandidateVotes['Percent_Khan']}% ({CandidateVotes['Khan']})")
    print(CandidateVotes['Percent_Correy'])
    print(CandidateVotes['Percent_Li'])
    print(CandidateVotes["Percent_O'Tooley"])
