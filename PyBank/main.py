import os
import csv

#path to budget data
budget_csv = os.path.join('Resources', 'budget_data.csv')
#Read through data
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

#Track what we are looking for in the data, may need to make others once loop is made
    TotalMonths = 0
    Month = []
    NetTotal = 0
    PLChangeList = []


    #Set at 0 since no previous month at first, set again in loop for previous month
    #Set PrevPL for first month, average not calculating correctly
    FirstMonthData = next(csvreader, None)
    FirstMonthPL = int(FirstMonthData[1])
    PrevPL = FirstMonthPL
   
    

    for row in csvreader:
        #Start with easiest problems first, get total months and total profit/loss
        #Convert data from file to integer
        TotalMonths += 1
        NetTotal += int(row[1])
        #Find the change between each month first, then find average outside of loop
        PLchange = int(row[1]) - int(PrevPL)
        #set previous profit/loss for the next iteration
        PrevPL = row[1]
        #Add to lists
        Month.append(row[0])
        PLChangeList.append(PLchange)





    AverageChange = round(sum(PLChangeList) / len(PLChangeList), 2)


    print("Financial Analysis")
    print('---------------------------')
    print(f'Total Months: {TotalMonths}')
    print(f'Total: ${NetTotal}')
    print(f'Average Change: ${AverageChange}')



