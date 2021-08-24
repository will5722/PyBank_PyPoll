import os
import csv

#path to budget data
budget_csv = os.path.join('Resources', 'budget_data.csv')
#Read through data
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#Track what we are looking for in the data
    TotalMonths = 0
    NetTotal = 0



