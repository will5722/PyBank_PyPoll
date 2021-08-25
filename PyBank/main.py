import os
import csv

#path to budget data
budget_csv = os.path.join('Resources', 'budget_data.csv')
#Read through data
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

#Track what we are looking for in the data, may need to make others once loop is made
    TotalMonths = 1
    Month = []
    NetTotal = 0
    PLChangeList = []


    #Set at 0 since no previous month at first, set again in loop for previous month
    #Set PrevPL for first month, average not calculating correctly otherwise
    FirstMonthData = next(csvreader, None)
    FirstMonthPL = int(FirstMonthData[1])
    PrevPL = FirstMonthPL
    NetTotal = int(FirstMonthData[1])

    

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


    #Find largest and smallest values in PLChange
    GreatestProfit = max(PLChangeList)
    GreatestLoss = min(PLChangeList)
    #Find the index of the above to find the corresponding month 
    ProfitMonthInd = PLChangeList.index(GreatestProfit)
    LossMonthInd = PLChangeList.index(GreatestLoss)
    #Use index to set the month
    ProfitMonth = Month[ProfitMonthInd]
    LossMonth = Month[LossMonthInd]

    #Go into list and find average change, round to 2 decimal places
    AverageChange = round(sum(PLChangeList) / len(PLChangeList), 2)

    #Print analysis in terminal
    print('Financial Analysis')
    print('---------------------------')
    print(f'Total Months: {TotalMonths}')
    print(f'Total: ${NetTotal}')
    print(f'Average Change: ${AverageChange}')
    print(f'Greatest Increase in Profits: {ProfitMonth} (${GreatestProfit}) ')
    print(f'Greatest Decrease in Profits: {LossMonth} (${GreatestLoss}) ')

#Export analysis to .txt file
output_file = os.path.join('Analysis', 'Financial_Analysis.txt')
with open(output_file, 'w')as txtfile:
    txtfile.write('Financial Analysis' + '\n')
    txtfile.write('---------------------------' + '\n')
    txtfile.write(f'Total Months: {TotalMonths}' + '\n')
    txtfile.write(f'Total: ${NetTotal}' + '\n')
    txtfile.write(f'Average Change: ${AverageChange}' + '\n')
    txtfile.write(f'Greatest Increase in Profits: {ProfitMonth} (${GreatestProfit}) ' + '\n')
    txtfile.write(f'Greatest Decrease in Profits: {LossMonth} (${GreatestLoss}) ' + '\n')
    
