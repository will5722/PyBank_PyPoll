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

    #Create new keys in dict for % of votes each candidate received


    