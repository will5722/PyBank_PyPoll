import os
import csv

#Path to election data
election_csv = os.path.join('Resources', 'election_data.csv')
#Open and read data
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

#Set variables/parameters to track
    TotalVotes = 0
    Candidates = []
    CandidateVotes = []



    for row in csvreader:
        Totalvotes =+ 1
        Candidates.append(row[2])
        

    