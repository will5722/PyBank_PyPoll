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



    for row in csvreader:
        Totalvotes =+ 1
        Name = row[2]
        CandidateList.append(row[2])


    