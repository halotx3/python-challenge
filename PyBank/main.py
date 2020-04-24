import os
import csv

budgetCSV = os.path.join("Resources", "budget_data.csv")

with open(budgetCSV, newline="") as budgetFile:
    csvreader = csv.reader(budgetFile, delimiter=",")
    #Setting variables that will be needed
    dateNum = 0
    profitloss = 0
    profits = []
    dates = []
    
    next(csvreader)
    # Getting all values needed from the row

    for row in csvreader:
        dateNum = dateNum + 1
        profitloss = int(row[1]) + profitloss
        profits.append(row[1])
        dates.append(row[0])

    maxprofits = max(profits)
    maxloss = min(profits)
    maxdate = dates[profits.index(maxprofits)]
    mindate = dates[profits.index(maxloss)]

    # print(maxprofits)
    profitlossAverage = "${:,.2f}".format(profitloss / dateNum)
    losses = "${:,.2f}".format(profitloss)
    #Creating the text output file
    file = open("output.txt", "w")
    file.write("Financial Review from 2010 to 2017 \n")
    file.write("------------------------------------ \n")
    file.write(f"Total Months Covered {dateNum} \n")
    file.write(f"Total Amount Made: {losses} \n")
    file.write(f"Monthly Average: {profitlossAverage} \n")
    file.write(f"The largest increase of profits came in {maxdate} bringing in {maxprofits} \n")
    file.write(f"The largest decrease was in {mindate} resulting in losses of {maxloss} \n")
    file.close()
    #Final Message delivered    
    file = open("output.txt", "r")

    print (file.read())
